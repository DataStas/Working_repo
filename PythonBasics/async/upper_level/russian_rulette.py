import asyncio


async def trigger(position):
    await asyncio.sleep(position)
    if position == 3:
        raise RuntimeError('Boooom!')
    print('%d is ok' % position)


async def russian_roulette():
    coros = (trigger(i) for i in range(8))
    try:
        await asyncio.gather(*coros)
    except RuntimeError as e:
        print(e)
    await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(russian_roulette())