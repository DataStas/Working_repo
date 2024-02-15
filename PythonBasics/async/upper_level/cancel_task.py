import asyncio

# Задача coro не будет прервана: лучше через shield!
async def coro_bad():
    print('start')
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print('ninja coroutine!')
    print('finished')


async def cancel(task):
    await asyncio.sleep(0.5)
    task.cancel()
    print('task.cancel() called')
    try:
        await task
    except asyncio.CancelledError:
        print('task successfully cancelled')


async def main_bad():
    task = asyncio.create_task(coro_bad())
    asyncio.create_task(cancel(task))
    await asyncio.sleep(5)
    assert task.cancelled()


async def coro():
    print('start')
    await asyncio.sleep(2)
    print('finished')


async def main():
    task = asyncio.create_task(coro())
    shielded = asyncio.shield(task)
    asyncio.create_task(cancel(shielded))
    await asyncio.sleep(5)
    assert not task.cancelled()


# async def main():
#     task = asyncio.create_task(coro())
#     shielded = asyncio.shield(task)
#     asyncio.create_task(cancel(shielded))
#     await shielded
#     assert not task.cancelled()

if __name__ == '__main__':
    asyncio.run(main_bad())
    asyncio.run(main())