import asyncio

from quarry.pc.proxy import proxy


async def bridge(source, sink, direction):
    while not source.is_closing():
        try:
            name, params = await source.read()
            sink.write(name, **params)
        except asyncio.IncompleteReadError:
            await source.close()
            await sink.close()


async def main():
    server = await proxy('127.0.0.1', 25565, '127.0.0.1', 25566, bridge)
    async with server:
        await server.serve_forever()


asyncio.run(main())
