import asyncio


async def eternity():
    try:
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('i was cancelled')
    raise print('finished')


async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout')


if __name__ == '__main__':
    asyncio.run(main())