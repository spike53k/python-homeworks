import asyncio
import time

async def job(name, seconds):
    print(f"{name}: начало")
    await asyncio.sleep(seconds)
    print(f"{name}: конец")

async def consistently():
    start_time = time.time()
    await job("A", 1)
    await job("B", 2)
    finish_time = time.time()
    print(f"Последовательно выполнилось за {finish_time - start_time} сек")

async def parallel():
    start_time = time.time()
    await asyncio.gather(job("A", 1), job("B", 2))
    finish_time = time.time()
    print(f"Параллельно выполнилось за {finish_time - start_time} сек")

async def main():
    await consistently()
    await parallel()

asyncio.run(main())