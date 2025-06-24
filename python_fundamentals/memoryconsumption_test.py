import asyncio

async def async_generator(n):
    for i in range(n):
        await asyncio.sleep(0.1)  # Simulate some async operation
        yield i

async def main():
    results = []
    async for item in async_generator(10):
        results.append(item)  # Data is stored in memory
        print(f"Processed: {item}")

    print(f"All results: {results}")

    print("Processing without storing:")
    async for item in async_generator(5):
        print(f"Processed: {item}") # Data is not stored after processing
if __name__ == "__main__":
    asyncio.run(main())