import asyncio
from utils.login import firstLogin


session, blink = asyncio.run(firstLogin())
for c in blink.cameras :
  print(c)

asyncio.run(session.close())