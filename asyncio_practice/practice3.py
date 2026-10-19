import asyncio

async def make_coffee():
    print("Кофе варится")
    await asyncio.sleep(3)
    print("Кофе готов")

async def make_sandwich():
    print("Бутерброд готовится")
    await asyncio.sleep(2)
    print("Бутерброд готов")

async def main():
    coffee = asyncio.create_task(make_coffee())
    sandwich = asyncio.create_task(make_sandwich())

    await sandwich
    print("Бутерброд готов, начинаю есть")
    await coffee
    print("Кофе готов, завтрак завершен")

asyncio.run(main())