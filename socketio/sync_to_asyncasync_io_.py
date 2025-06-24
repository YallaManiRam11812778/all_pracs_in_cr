import time
import asyncio

async def f():
    print("f started")
    await asyncio.sleep(3)
    print("f finished")

async def babu():
    print("$$$$$$$$$$$")
    # async def bab():
    #     print("^^^^^^^^^^^^^^^^^")
    asyncio.run(f())#threading.Thread(target=f).start()

# if __name__ == "__main__":
#     asyncio.run(babu())
