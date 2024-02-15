import asyncio


def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()
    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(None, blocking_io)
    print('default thread pool', result)


if __name__ == "__main__":
    asyncio.run(main())