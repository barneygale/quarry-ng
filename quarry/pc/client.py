import asyncio
import json

from quarry import crypto
from quarry.stream import FrameStream, PacketStream
from quarry.pc.auth import Profile


async def connect(host, port, version=None, mode='login'):
    reader, writer = await asyncio.open_connection(host, port)
    frames = FrameStream(reader, writer)
    stream = PacketStream(frames, edition='pc', version=version, client=True)
    stream.write(
        'set_protocol',
        protocolVersion=stream.version,
        serverHost=host,
        serverPort=port,
        nextState=1 if mode == 'status' else 2)
    stream.mode = mode
    return stream


async def status(host, port, version=None):
    stream = await connect(host, port, version=version, mode='status')
    stream.write('ping_start')
    params = await stream.expect('server_info')
    await stream.close()
    return json.loads(params['response'])


async def login(host, port, version=None, profile=None):
    if version is None:
        response = await status(host, port)
        version = response['version']['protocol']
    if profile is None:
        profile = Profile()

    stream = await connect(host, port, version=version, mode='login')
    stream.write('login_start', username=profile.display_name)

    while True:
        name, params = await stream.read()

        if name == 'disconnect':
            raise ValueError("Disconnected: %r" % params['reason'])

        elif name == 'login_plugin_request':
            stream.write(
                'login_plugin_response',
                messageId=params['messageId'],
                data=None)

        elif name == 'encryption_begin':
            key = crypto.unpack_public_key(params['publicKey'])
            shared_secret = crypto.make_shared_secret()
            digest = crypto.make_digest(
                params['serverId'].encode('ascii'),
                shared_secret,
                params['publicKey'])
            await profile.join(digest)
            stream.write(
                'encryption_begin',
                sharedSecret=crypto.encrypt_secret(key, shared_secret),
                verifyToken=crypto.encrypt_secret(key, params['verifyToken']))
            stream.encryption.enable(crypto.make_cipher(shared_secret))

        elif name == 'compress':
            stream.compression.enable(params['threshold'])

        elif name == 'success':
            stream.mode = 'play'
            break

    return stream
