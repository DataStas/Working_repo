import asyncio


async def main():
    print(await asyncio.sleep(1, 'hello'))

if __name__ == '__main__':
    asyncio.run(main())
