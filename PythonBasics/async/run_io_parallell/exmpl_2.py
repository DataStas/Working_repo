import asyncio


def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()
    # 2. Run in a custom thread pool:
    with asyncio.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print('custom thread pool', result)
    # 3. Run in a custom process pool:
    with asyncio.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print('custom process pool', result)

if __name__ == '__main__':
    asyncio.run(main())