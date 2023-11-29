import asyncio
from utils.login import login
from utils.arm import armSyncModule, armCamera
import click

@click.command()
@click.option("--mode", default="leave", help="arm mode to set, possible mode are leave, home, sleep, disable")
def setMode(mode):
    asyncio.run(setModeAsync(mode))


async def setModeAsync(mode):
    """Setting the Pre-Configuration Mode"""
    blink = await login()
    # Get sync module name, I only have 1 sync module so take the first one.
    keys = list(blink.sync.keys())
    syncModuleName = keys[0]

    if mode.lower() == "disable":
        await armSyncModule(blink, syncModuleName, False)
    else:
        await armSyncModule(blink, syncModuleName, True)
        if mode.lower() == "home":
            await armCamera(blink, "sidewalk", False)
            await armCamera(blink, "door", True)
            await armCamera(blink, "livingroom", False)
        elif mode.lower() == "sleep":
            await armCamera(blink, "sidewalk", True)
            await armCamera(blink, "door", True)
            await armCamera(blink, "livingroom", True)
        elif mode.lower() == "leave":
            await armCamera(blink, "sidewalk", False)
            await armCamera(blink, "door", True)
            await armCamera(blink, "livingroom", True)

if __name__ == '__main__':
    setMode()
  