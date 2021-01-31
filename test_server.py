import asyncio

from quarry.pc.server import listen

async def status(stream):
    return {'version': {'name': '1.16.4', 'protocol': 754},
            'players': {'max': 100, 'online': 0},
            'description': {'text': 'blah'}}


async def login(stream, profile):
    await stream.kick('blah')


async def main():
    server = await listen('127.0.0.1', 25565, status, login)
    async with server:
        await server.serve_forever()


asyncio.run(main())
