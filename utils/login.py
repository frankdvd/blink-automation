import asyncio
from aiohttp import ClientSession
from blinkpy.blinkpy import Blink
from blinkpy.auth import Auth
from blinkpy.helpers.util import json_load


credential_path = "../blink_credential.json"

async def firstLogin():
    session=ClientSession()
    blink = Blink(session=session)
    await blink.start()
    await blink.save(credential_path)
    return session, blink

async def login():
    blink = Blink()
    auth = Auth(await json_load(credential_path))
    blink.auth = auth
    await blink.start()
    return blink