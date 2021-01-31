import importlib
import io
import zlib

from quarry import chat, native

varint = native.VarInt()
imp = importlib.import_module


class Compression(object):
    threshold = None

    def compress(self, data):
        if self.threshold is not None:
            if len(data) < self.threshold:
                data = varint.pack(0) + data
            else:
                data = varint.pack(len(data)) + zlib.compress(data)
        return data

    def decompress(self, data):
        if self.threshold is not None:
            buff = io.BytesIO(data)
            length = varint.unpack(buff)
            data = buff.read()
            if length > 0:
                data = zlib.decompress(data)
        return data

    def enable(self, threshold):
        self.threshold = threshold


class Encryption(object):
    def encrypt(self, data):
        return data

    def decrypt(self, data):
        return data

    def enable(self, cipher):
        self.encrypt = cipher.encryptor().update
        self.decrypt = cipher.decryptor().update


class FrameStream(object):
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.encryption = Encryption()
        self.compression = Compression()
        self.addr = writer.get_extra_info('peername')[0]

    def __repr__(self):
        cls = type(self).__name__
        return "<%s addr=%r>" % (cls, self.addr)

    async def read(self):
        data = b""
        while True:
            byte = await self.reader.readexactly(1)
            byte = self.encryption.decrypt(byte)
            data += byte
            if not byte[0] & 0x80:
                break
        length = varint.unpack(io.BytesIO(data))
        data = await self.reader.readexactly(length)
        data = self.encryption.decrypt(data)
        data = self.compression.decompress(data)
        return io.BytesIO(data)

    def write(self, *data):
        data = b"".join(data)
        data = self.compression.compress(data)
        data = varint.pack(len(data)) + data
        data = self.encryption.encrypt(data)
        self.writer.write(data)

    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

    def is_closing(self):
        return self.writer.is_closing()


class PacketStream(object):
    def __init__(self, parent, edition, version=None, mode=None, client=False):
        self.parent = parent
        self.edition = edition
        self.version = version or imp("quarry.%s.data" % edition).version
        self.module = imp("quarry.%s.data.v%04d" % (edition, self.version))
        self.mode = mode or 'init'
        self.client = client

    def __repr__(self):
        return "<%s parent=%r, edition=%r, version=%r, mode=%r, client=%r>" \
               % (type(self).__name__, self.parent, self.edition, self.version,
                  self.mode, self.client)

    def __getattr__(self, name):
        return getattr(self.parent, name)

    def _type(self, direction):
        return getattr(self.module, 'packet_%s_%s' % (self.mode, direction))

    async def read(self):
        type = self._type("down" if self.client else "up")
        buff = await self.parent.read()
        data = type.unpack(buff)
        assert buff.read() == b''
        return data['name'], data['params']

    async def expect(self, name):
        p_name, p_params = await self.read()
        if name != p_name:
            raise ValueError("Expected %r but received %r" % (name, p_name))
        return p_params

    def write(self, name, **params):
        type = self._type("up" if self.client else "down")
        data = {'name': name, 'params': params}
        data = type.pack(data)
        self.parent.write(data)

    async def kick(self, reason):
        reason = chat.pack(reason)
        if not self.client:
            if self.mode == 'login':
                self.write('disconnect', reason=reason)
            elif self.mode == 'play':
                self.write('kick_disconnect', reason=reason)
        await self.parent.close()