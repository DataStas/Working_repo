import asyncio


async def my_sleep(delay):
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    loop.call_later(delay, future.set_result, True)
    await future


async def main():
    loop = asyncio.get_running_loop()
    print(loop.time()) # 0.9779213
    await my_sleep(1)
    print(loop.time()) # 1.979251479

if __name__ == '__main__':
    asyncio.run(main())
