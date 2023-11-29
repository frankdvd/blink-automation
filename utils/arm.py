
async def armSyncModule(blink, syncModuleName, isArm):
    # Arm/Disarm a sync module
    await blink.sync[syncModuleName].async_arm(isArm)
    # Print arm status of a sync module - a system refresh should be performed first
    await blink.refresh()
    sync = blink.sync[syncModuleName]
    print(f"{sync.name} status: {sync.arm}")

async def armCamera(blink, CameraName, isArm):
    # Arm/Disarm a camera
    await blink.cameras[CameraName].async_arm(isArm)
    # Print arm status of a sync module - a system refresh should be performed first
    await blink.refresh()
    camera = blink.cameras[CameraName]
    print(f"{camera.name} status: {camera.arm}")