import asyncio

async def fetch_data(user):
    print("Fetching data +++++++++++ ")
    await asyncio.sleep(2) #
    await summ(user)
    await subb(user)
    return [{"message":"Data sending from api method"}]

async def summ(user):
    await asyncio.sleep(1)
    print(f"sum......... for {user}")
    await asyncio.sleep(1)

async def subb(user):
    await asyncio.sleep(1)
    print(f"subbbbbb ......... { user}")
    await asyncio.sleep(1)
