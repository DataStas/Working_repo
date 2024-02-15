import asyncio
import random


async def update_rate():
    global rate
    while True:
        rate = random.randint(1, 99)
        await asyncio.sleep(3)


def handle():
    pass


async def main():
    asyncio.create_task(update_rate())
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())