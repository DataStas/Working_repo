import aiohttp
import asyncio


async def check_user_exists(user_id: int) -> bool:
    async with aiohttp.ClientSession() as session:
        url = f'https://example.org/users/{user_id}'
        async with session.head(url) as resp:
            print(user_id, resp.status == 200)
            return resp.status == 200


async def main_slow(): # slow bad
    for i in range(100):
        await check_user_exists(1)


async def main_big(): # works, but big
    future = asyncio.get_running_loop().create_future()
    tasks = []
    executing = 0

    def cb(task):
        nonlocal executing
        executing -= 1
        if executing == 0:
            future.set_result([task.result() for task in tasks])
    for i in range(100):
        task = asyncio.create_task(check_user_exists(i))
        task.add_done_callback(cb)
        executing += 1
        tasks.append(task)
    await future
    print(future.result())


# asyncio.gather() запускает указанные awaitable объекты в
# конкурентном режиме и возвращает результаты выполнения в том же
# порядке
# Оборачивает объекты coroutine в asyncio.Task

async def main():
    coros = (
        check_user_exists(i)
        for i in range(100)
    )
    # <class 'list'>: [False, False, ...]
    results = await asyncio.gather(*coros)


async def main_bad_example():
    coros = (
        check_user_exists(i)
        for i in range(100)
    )
    asyncio.gather(*coros)
    await asyncio.sleep(10)

if __name__ == '__main__':
    check_user_exists(1)
