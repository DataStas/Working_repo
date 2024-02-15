import asyncio


async def main():
    tasks = [
        asyncio.create_task(check_user_exists(i))
        for i in range(100)
    ]
    done, pending = await asyncio.wait(
    tasks, return_when=asyncio.FIRST_EXCEPTION
    )
    # done: <class 'set'>: {<Task finished coro=...>}
    # pending: <class 'set'>: {<Task finished coro=...>}
    print(done, pending)

asyncio.run(main())