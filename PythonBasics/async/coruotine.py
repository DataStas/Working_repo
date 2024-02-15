import asyncio
import time


def dec(funс: callable):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f'Функция {funс.__name__} вызвана {counter} раз')
        return funс(*args, **kwargs)
    return wrapper

@dec
async def get_text(delay: int, text: str) -> str:
    await asyncio.sleep(delay)
    return text

@dec
async def say_text():
    task1 = asyncio.create_task(get_text(1, 'hello')) # задача создана в event loop, но не выполняется
    task2 = asyncio.create_task(get_text(1, 'world'))
    await task1  # задача выполяется
    await task2
    return ', '.join([task1.result(), task2.result()])





if __name__ == "__main__":
    result = asyncio.run(say_text())
    print(result)