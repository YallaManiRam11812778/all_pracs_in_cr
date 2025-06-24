import asyncio
import api

async def data_sending(user:str):
    print(f"request by  ---------  {user}")

async def get_list():
    await data_sending("admin")
    fetched_data = await asyncio.gather(api.fetch_data("Ram"), api.fetch_data("Lakshman"))
    print("fetched_data ======== ",fetched_data)

if __name__ == "__main__":
    asyncio.run(get_list())