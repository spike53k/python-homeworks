import asyncio

async def greet(name):
    print(f"Привет, {name}!")
    await asyncio.sleep(1)
    print(f"Пока, {name}!")


asyncio.run(greet("Name1"))