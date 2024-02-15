import asyncio

async def get_text():
    return 'Hello World'

async def say_hello():
    text = await get_text()
    await asyncio.sleep(1)
    return text

if __name__ == "__main__":
    result = asyncio.run(say_hello())
    print(result)