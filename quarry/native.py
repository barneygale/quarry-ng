from dataclasses import dataclass
import json
import struct
import uuid


from quarry.nbt import TagRoot


def ref(path, context):
    idx = -1
    while path.startswith('../'):
        path = path[3:]
        idx -= 1
    val = context[idx]
    for part in path.split('/'):
        val = val[part]
    return val


class AbstractType(object):
    def pack(self, item, context=()):
        raise NotImplementedError

    def unpack(self, buff, context=()):
        raise NotImplementedError


@dataclass
class Void(AbstractType):
    def pack(self, item, context=()):
        return b''

    def unpack(self, buff, context=()):
        return None


@dataclass
class Container(AbstractType):
    fields: list

    def pack(self, item, context=()):
        out = b''
        for field in self.fields:
            type = field['type']
            anon = field.get('anon')
            data = item if anon else item[field['name']]
            out += type.pack(data, context + (item,))
        return out

    def unpack(self, buff, context=()):
        item = {}
        for field in self.fields:
            val = field['type'].unpack(buff, context + (item,))
            if field.get('anon'):
                if val:
                    item.update(val)
            else:
                item[field['name']] = val
        return item


@dataclass
class Switch(AbstractType):
    fields: dict
    compareTo: str = None
    default: AbstractType = None

    def type(self, context):
        val = ref(self.compareTo, context)
        if isinstance(val, bool):
            val = 'true' if val else 'false'
        elif isinstance(val, int):
            val = str(val)
        else:
            assert isinstance(val, str)
        return self.fields.get(val, self.default)

    def pack(self, item, context=()):
        return self.type(context).pack(item, context)

    def unpack(self, buff, context=()):
        return self.type(context).unpack(buff, context)


@dataclass
class Option(AbstractType):
    type: AbstractType

    def pack(self, item, context=()):
        if item is None:
            return b'\x00'
        else:
            return b'\x01' + self.type.pack(item, context)

    def unpack(self, buff, context=()):
        if buff.read(1) == b'\x00':
            return None
        else:
            return self.type.unpack(buff, context)


@dataclass
class Mapper(AbstractType):
    type: AbstractType
    mappings: dict

    def pack(self, item, context=()):
        # FIXME: slow
        for key, val in self.mappings.items():
            if val == item:
                key = int(key, 16)
                return self.type.pack(key, context)
        raise KeyError(item)

    def unpack(self, buff, context=()):
        key = self.type.unpack(buff, context)
        key = '0x%02x' % key
        return self.mappings[key]


@dataclass
class Struct(AbstractType):
    fmt: str

    def pack(self, item, context=()):
        return struct.pack(self.fmt, item)

    def unpack(self, buff, context=()):
        return struct.unpack(self.fmt, buff.read(struct.calcsize(self.fmt)))[0]


@dataclass
class VarInt(AbstractType):
    bits: int = 32

    def pack(self, item, context=()):
        if item < 0:
            item += 1 << self.bits
        data = b''
        for i in range(1 + (self.bits - 1) // 7):
            b = item & 0x7F
            item >>= 7
            if item > 0:
                data += bytes([b | 0x80])
            else:
                data += bytes([b])
                break
        return data

    def unpack(self, buff, context=()):
        item = 0
        for i in range(1 + (self.bits - 1) // 7):
            b = buff.read(1)[0]
            item |= (b & 0x7F) << 7 * i
            if not b & 0x80:
                break
        if item & (1 << (self.bits - 1)):
            item -= 1 << self.bits
        return item


@dataclass
class UUID(AbstractType):
    def pack(self, value, context=()):
        return value.bytes

    def unpack(self, buff, context=()):
        return uuid.UUID(bytes=buff.read(16))


@dataclass
class BitField(AbstractType):
    fields: list

    @property
    def size(self):
        return sum(field['size'] for field in self.fields)

    @property
    def fmt(self):
        return {8: 'B', 16: '>H', 32: '>I', 64: '>Q'}[self.size]

    def pack(self, item, context=()):
        out = 0
        for field in self.fields:
            out <<= field['size']
            unused = field['name'] in ('unused', '_unused')
            if not unused:
                val = item[field['name']]
                if field['signed'] and val < 0:
                    val = val + (1 << field['size'])
                out |= val
        return struct.pack(self.fmt, out)

    def unpack(self, buff, context=()):
        item = {}
        data = struct.unpack(self.fmt, buff.read(struct.calcsize(self.fmt)))[0]
        for field in reversed(self.fields):
            unused = field['name'] in ('unused', '_unused')
            if not unused:
                mask = (1 << field['size']) - 1
                val = data & mask
                if field['signed'] and val & (1 << (field['size'] - 1)):
                    val = val - (1 << field['size'])
                item[field['name']] = val
            data >>= field['size']
        assert data == 0
        return item


@dataclass
class NBT(AbstractType):
    def pack(self, value, context=()):
        if value is None:
            return b'\x00'
        return value.pack()

    def unpack(self, buff, context=()):
        return TagRoot.unpack(buff)


@dataclass
class String(AbstractType):
    countType: AbstractType

    def pack(self, item, context=()):
        item = item.encode('utf-8')
        return self.countType.pack(len(item), context) + item

    def unpack(self, buff, context=()):
        length = self.countType.unpack(buff, context)
        return buff.read(length).decode('utf-8')


@dataclass
class Array(AbstractType):
    type: AbstractType
    count: 'typing.Any' = None
    countType: AbstractType = None

    def pack(self, item, context=()):
        out = b''
        if self.countType:
            out += self.countType.pack(len(item), context)
        for val in item:
            out += self.type.pack(val, context)
        return out

    def unpack(self, buff, context=()):
        if self.countType:
            count = self.countType.unpack(buff, context)
        elif isinstance(self.count, str):
            count = ref(self.count, context)
        else:
            count = self.count
        return [self.type.unpack(buff, context) for _ in range(count)]


@dataclass
class ByteArray(AbstractType):
    count: 'typing.Any' = None
    countType: AbstractType = None

    def pack(self, item, context=()):
        out = b''
        if self.countType:
            out += self.countType.pack(len(item), context)
        out += item
        return out

    def unpack(self, buff, context=()):
        if self.countType:
            count = self.countType.unpack(buff, context)
        elif isinstance(self.count, str):
            count = ref(self.count, context)
        else:
            count = self.count
        return buff.read(count)


@dataclass
class EntityMetadataArray(AbstractType):
    type: AbstractType
    endVal: int

    def pack(self, item, context=()):
        out = b''
        for row in item:
            out += bytes([row['key']])
            out += VarInt().pack(row['type'], context + (row,))
            out += self.type.pack(row['value'], context + (row,))
        return out + bytes([self.endVal])

    def unpack(self, buff, context=()):
        item = []
        while True:
            row = {'key': buff.read(1)[0]}
            if row['key'] == self.endVal:
                break
            row['type'] = VarInt().unpack(buff, context + (row,))
            row['value'] = self.type.unpack(buff, context + (row,))
            item.append(row)
        return item


@dataclass
class EntityEquipmentArray(AbstractType):
    type: AbstractType

    def pack(self, item, context=()):
        out = b''
        rows = list(item)
        while rows:
            row = rows.pop(0)
            if rows:
                out += bytes([row['slot'] | 0x80])
            else:
                out += bytes([row['slot']])
            out += self.type.pack(row['item'], context)
        return out

    def unpack(self, buff, context=()):
        rows = []
        while True:
            row = {
                'slot': buff.read(1)[0],
                'item': self.type.unpack(buff, context)
            }
            rows.append(row)
            if row['slot'] & 0x80:
                row['slot'] &= 0x7F
            else:
                break
        return rows


@dataclass
class Count(AbstractType):
    type: AbstractType
    countFor: str

    def pack(self, item, context=()):
        return self.type.pack(item, context)

    def unpack(self, buff, context=()):
        return self.type.unpack(buff, context)
