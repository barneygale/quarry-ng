import json
import os
import sys
from uuid import UUID, uuid3


import aiohttp


auth_server_url = "https://authserver.mojang.com/"
session_server_url = "https://sessionserver.mojang.com/"


def accounts_path():
    dot_minecraft = ".minecraft"
    if sys.platform == 'win32':
        app_data = os.environ['APPDATA']
    elif sys.platform == 'darwin':
        app_data = os.path.expanduser("~/Library/Application Support")
        dot_minecraft = "minecraft"
    else:
        app_data = os.path.expanduser("~")
    return os.path.join(app_data, dot_minecraft, "launcher_accounts.json")


async def expect_status(response, status):
    if response.status != status:
        raise AuthError(
            "Unexpected response (%d) for URL %r. Detail: %r" %
            (response.status, response.url, await response.json()))


class AuthError(Exception):
    pass


class OfflinePlayerNamespace(object):
    bytes = b'OfflinePlayer:'


class Profile(object):
    def __init__(self, display_name=None, uuid=None):
        self.display_name = display_name or "quarry"
        self.uuid = uuid or uuid3(OfflinePlayerNamespace(), self.display_name)

    def join(self, digest):
        raise AuthError("Can't join online-mode server with offline profile")

    async def has_joined(self, digest, address=None):
        url = session_server_url + "session/minecraft/hasJoined"
        params = {
            'username': self.display_name,
            'serverId': digest,
        }
        if address is not None:
            params['ip'] = address

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                await expect_status(response, 200)
                data = await response.json()
                return type(self)(data['name'], UUID(hex=data['id']))


class MojangProfile(Profile):
    def __init__(self, display_name, uuid, client_token, access_token):
        super().__init__(display_name, uuid)
        self.client_token = client_token
        self.access_token = access_token

    async def join(self, digest):
        data = {
            'accessToken': self.access_token,
            'selectedProfile': self.uuid.hex,
            'serverId': digest
        }
        url = session_server_url + "session/minecraft/join"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                await expect_status(response, 204)

    async def refresh(self):
        async with aiohttp.ClientSession() as session:
            data = {
                'accessToken': self.access_token,
                'clientToken': self.client_token
            }
            url = auth_server_url + "validate"
            async with session.post(url, json=data) as response:
                if response.status == 204:
                    return

            url = auth_server_url + "refresh"
            async with session.post(url, json=data) as response:
                await expect_status(response, 200)


    @classmethod
    async def from_credentials(cls, email, password):
        async with aiohttp.ClientSession() as session:
            data = {
                'username': email,
                'password': password,
                'agent': {'name': 'Minecraft', 'version': 1},
                'clientToken': 'foo'  # FIXME: randomize
            }
            url = auth_server_url + "authenticate"
            async with session.post(url, json=data) as response:
                await expect_status(response, 200)
                response = response.json()
                return cls(
                    response['selectedProfile']['name'],
                    UUID(hex=response['selectedProfile']['id']),
                    response['clientToken'],
                    response['accessToken'])

    @classmethod
    def from_file(cls, display_name=None, uuid=None, path=None):
        if path is None:
            path = accounts_path()

        with open(path) as fd:
            data = json.load(fd)

        if display_name is None and uuid is None:
            account = data['accounts'][data["activeAccountLocalId"]]
        else:
            for account in data["accounts"].values():
                if display_name == account["minecraftProfile"]["name"]:
                    break
                if uuid == UUID(hex=account["minecraftProfile"]["id"]):
                    break
            else:
                raise AuthError("Profile not found.")

        display_name = account['minecraftProfile']['name']
        uuid = UUID(hex=account["minecraftProfile"]["id"])
        client_token = data["mojangClientToken"]
        access_token = account['accessToken']
        return cls(display_name, uuid, client_token, access_token)
