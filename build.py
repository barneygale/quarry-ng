from argparse import ArgumentParser
from functools import partial
from collections import ChainMap
from copy import deepcopy
from json import load
from pathlib import Path

from quarry.native import *


types = {
    # Containers/logic
    'void': Void,
    'container': Container,
    'switch': Switch,
    'option': Option,
    'mapper': Mapper,

    # Simple types
    'i8':  partial(Struct, 'b'),  'u8':  partial(Struct, 'B'),
    'i16': partial(Struct, '>h'), 'u16': partial(Struct, '>H'),
    'i32': partial(Struct, '>i'), 'u32': partial(Struct, '>I'),
    'i64': partial(Struct, '>q'),
    'f32': partial(Struct, '>f'),
    'f64': partial(Struct, '>d'),
    'bool': partial(Struct, '?'),
    'varint': VarInt,
    'UUID': UUID,
    'bitfield': BitField,

    # Length-prefixed types
    'pstring': String,
    'array': Array,
    'buffer': ByteArray, 'restBuffer': ByteArray,

    # Other array types
    'entityMetadataLoop': EntityMetadataArray,
    'topBitSetTerminatedArray': EntityEquipmentArray,

    # NBT
    'nbt': NBT, 'optionalNbt': NBT, 'compressedNbt': NBT,

    # TODO: describe
    'count': Count,
}


def main_cli():
    parser = ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    main(args.input)


def main(in_path):
    in_path = Path(in_path)
    out_path = Path('quarry')
    index_path = in_path / 'dataPaths.json'


    with index_path.open() as f:
        index = load(f)

    for edition, releases in index.items():
        if edition == 'pe':
            continue  # TODO: PE support

        edition_path = out_path / edition / 'data'
        default_version = 0
        for release, fields in releases.items():
            if release == '0.30c':
                continue  # TODO: Classic support

            # Load the protocol
            protocol_path = in_path / fields['protocol'] / 'protocol.json'
            with protocol_path.open() as f:
                protocol = load(f)

            # Load the version
            version_path = in_path / fields['version'] / 'version.json'
            with version_path.open() as f:
                version = load(f)['version']

            # Update the default version
            default_version = max(default_version, version)

            # Write the version module
            module_name = 'v%04d.py' % version
            module_path = edition_path / module_name
            with module_path.open('w') as f:
                f.write('# !!! auto-generated - do not edit !!!\n')
                f.write('from quarry.native import *\n')
                f.write('edition = %r\n' % edition)
                f.write('release = %r\n' % release)
                f.write('version = %r\n' % version)
                for mode, direction, type in walk(protocol):
                    f.write('packet_%s_%s = %r\n' % (mode, direction, type))

        # Write the edition module
        module_name = '__init__.py'
        module_path = edition_path / module_name
        with module_path.open('w') as f:
            f.write('# !!! auto-generated - do not edit !!!\n')
            f.write('version = %r\n' % default_version)


def walk(protocol, parents=None, context=None):
    # Defaults
    if parents is None:
        parents = tuple()
    if context is None:
        context = ChainMap()

    # Load types
    if 'types' in protocol:
        context = context.new_child(protocol['types'])

    # Walk child namespaces
    for key, val in protocol.items():
        if key != 'types':
            # Fix naming
            key = {
                'handshaking': 'init',
                'toServer': 'up',
                'toClient': 'down'
            }.get(key, key)
            yield from walk(val, parents + (key,), context)

    # Compile this namespace
    for packet_type in ('packet', 'mcpe_packet'):
        if packet_type in context:
            mode, direction = parents
            yield mode, direction, compile(context[packet_type], context)


def compile(obj, context):
    # Resolve to a native type
    prev = {}
    while True:
        # Split name/args
        if isinstance(obj, str):
            name, args = obj, {}
        elif len(obj) == 1:
            name, args = obj[0], {}
        else:
            name, args = obj[0], deepcopy(obj[1])

        # Fix up arguments
        if name in ('container', 'bitfield'):
            args = {'fields': args}
        elif name == 'option':
            args = {'type': args}
        elif name == 'entityMetadataLoop':
            args['type'] = ['entityMetadataItem', {'compareTo': 'type'}]
        elif name == 'topBitSetTerminatedArray':
            args['type'] = 'slot'
        assert isinstance(args, dict)

        # Resolve links to previous arguments
        args = prev = {key: isinstance(val, str) and val[0] == '$' and
                       prev[val[1:]] or val for key, val in args.items()}

        # Find the next call in the chain
        obj = context.get(name, 'native')
        if obj == 'native':
            break

    # Compile arguments
    for arg in ('default', 'type', 'countType'):
        if arg in args:
            args[arg] = compile(args[arg], context)
    if name == 'switch':
        args['fields'] = {key: compile(val, context)
                          for key, val in args['fields'].items()}
    if name == 'container':
        for field in args['fields']:
            field['type'] = compile(field['type'], context)

    # Instantiate type
    return types[name](**args)


if __name__ == '__main__':
    main_cli()
