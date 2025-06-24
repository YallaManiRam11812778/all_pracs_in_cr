import asyncio
from functools import wraps

# Decorator to run a function asynchronously
def make_async(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return async_wrapper

# Example synchronous function
def sync_function(x):
    print(f"Processing {x}")
    return x * 2

# Applying the decorator to make it asynchronous
async_function = make_async(sync_function)

# Using the async version in an async context
async def main():
    result = await async_function(5)
    print(result)

# Running the async function
asyncio.run(main())
