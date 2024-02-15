import asyncio
import time


async def get_text():
    await asyncio.sleep(3)
    return 'Hello World'


async def say_hello():
    text = await get_text()
    print(f'Second {time.ctime()}')
    await asyncio.sleep(1)
    print(f'Third {time.ctime()}')
    return text

if __name__ == "__main__":
    print(f'First {time.ctime()}')
    result = asyncio.run(say_hello())
    print(f'Last {time.ctime()}')
    print(result)


# First Thu Feb 15 17:38:28 2024
# Second Thu Feb 15 17:38:31 2024
# Third Thu Feb 15 17:38:32 2024
# Last Thu Feb 15 17:38:32 2024
# Hello World