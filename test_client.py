import asyncio

from quarry.pc.auth import MojangProfile
from quarry.pc.client import status, login

async def main():
    # Get the server status
    response = await status('127.0.0.1', 25566)
    print(response)

    # Get a profile
    profile = MojangProfile.from_file()
    await profile.refresh()

    # Login
    stream = await login('127.0.0.1', 25566, profile=profile)

    # Read a packet
    name, params = await stream.read()
    print(name, params)

    # Close connection
    await stream.close()


asyncio.run(main())


