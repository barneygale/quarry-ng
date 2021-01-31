import asyncio

from quarry.pc.client import status, login
from quarry.pc.server import listen


async def proxy(listen_host, listen_port, host, port, bridge_callback, **kw):

    async def _status(server):
        response = await status(host, port, server.version)
        return response

    async def _login(server, profile):
        client = await login(host, port, server.version, profile)
        await asyncio.gather(
            bridge_callback(server, client, "up"),
            bridge_callback(client, server, "down"))

    return await listen(listen_host, listen_port, _status, _login, **kw)
