import time
import asyncio


async def process(resq):
    await asyncio.sleep(5)
    print("hello world")

loop = asyncio.get_event_loop()
sdt = time.time()
res = loop.run_until_complete(process("fdas"))
print(time.time()-sdt)
