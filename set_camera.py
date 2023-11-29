import asyncio
from utils.login import login
from utils.arm import armSyncModule, armCamera
import click

@click.command()
@click.option("--camera", default="leave", help="camera name, possible name are sidewalk, door, livingroom")
@click.option("--arm", default=True, help="arm the camera or not")
def setCamera(camera, arm):
    asyncio.run(setCameraAsync(camera, arm))


async def setCameraAsync(camera, arm):
    """Setting camera motion detection"""
    blink = await login()
    # Get sync module name, I only have 1 sync module so take the first one.
    keys = list(blink.sync.keys())
    syncModuleName = keys[0]

    if blink.sync[syncModuleName].arm == False and arm == True:
        await armSyncModule(blink, syncModuleName, True)
    await armCamera(blink, camera, arm)
    

if __name__ == '__main__':
    setCamera()
  