import asyncio
import time

async def hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    test_data = [("Name1", 1), ("Name2", 1), ("Name3", 1)]

    start_time = time.time()
    for name, delay in test_data:
        await hello(name, delay)
    end_time = time.time()
    finish_time = end_time - start_time

    print(f"Время выполнения: {finish_time}")

    start_time = time.time()
    await asyncio.gather(hello("Name1", 1), hello("Name2", 1), hello("Name3", 1))
    end_time = time.time()
    finish_time = end_time - start_time

    print(f"Время выполнени: {finish_time}")

if __name__ == "__main__":
    asyncio.run(main())