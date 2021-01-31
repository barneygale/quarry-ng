import asyncio
import json

from quarry import crypto
from quarry.stream import FrameStream, PacketStream
from quarry.pc.auth import Profile, AuthError


async def listen(host, port, status_callback, login_callback, online=True,
                 allow_proxies=False, compression_threshold=256, **kwargs):

    key = crypto.make_keypair()

    async def handler(reader, writer):
        frames = FrameStream(reader, writer)
        stream = PacketStream(frames, 'pc')
        params = await stream.expect('set_protocol')
        version = params['protocolVersion']
        mode = 'status' if params['nextState'] == 1 else 'login'
        stream = PacketStream(frames, 'pc', version=version, mode=mode)

        if stream.mode == 'status':
            await stream.expect('ping_start')
            status = await status_callback(stream)
            stream.write('server_info', response=json.dumps(status))
            params = await stream.expect('ping')
            stream.write('ping', **params)
            return await stream.close()

        params = await stream.expect('login_start')
        profile = Profile(params['username'])

        if compression_threshold:
            stream.write('compress', threshold=compression_threshold)
            stream.compression.enable(compression_threshold)

        if online:
            server_id = crypto.make_server_id()
            public_key = crypto.pack_public_key(key)
            verify_token = crypto.make_verify_token()
            stream.write(
                'encryption_begin',
                serverId=server_id.decode('ascii'),
                publicKey=public_key,
                verifyToken=verify_token)
            params = await stream.expect('encryption_begin')
            shared_secret = crypto.decrypt_secret(key, params['sharedSecret'])
            verify_token2 = crypto.decrypt_secret(key, params['verifyToken'])
            digest = crypto.make_digest(server_id, shared_secret, public_key)
            address = None if allow_proxies else stream.addr
            stream.encryption.enable(crypto.make_cipher(shared_secret))
            try:
                profile = await profile.has_joined(digest, address)
            except AuthError:
                return await stream.kick('Auth failed (session)')
            if verify_token != verify_token2:
                return await stream.kick('Auth failed (token)')

        stream.write(
            'success',
            uuid=profile.uuid,
            username=profile.display_name)
        stream.mode = 'play'
        await login_callback(stream, profile)

    server = await asyncio.start_server(handler, host, port, **kwargs)
    return server
