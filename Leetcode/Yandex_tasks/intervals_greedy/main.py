import random
from typing import Tuple


def intersec(inter: list) -> int:
    inter.sort(key=lambda x: x[1])  # Сортируем интервалы по правому концу
    count = 0
    end = float('-inf')  # Инициализируем переменную для хранения конца предыдущего интервала
    for interval in inter:
        if interval[0] > end:  # Если начало текущего интервала больше конца предыдущего
            count += 1
            end = interval[1]  # Обновляем конец предыдущего интервала
    return count


def test(num, bounds: list[int]):
    intervals = []
    for _ in range(num):
        c1 = [random.randint(bounds[0], bounds[1]) for _ in range(2)]
        if c1[0] > c1[1]:
            c1[0], c1[1] = c1[1], c1[0]
        intervals.append(tuple(c1))
    print(intervals)
    return intervals


if __name__ == '__main__':
    num = int(input())
    intervals = []
    for _ in range(num):
        intervals.append(tuple(map(int, input().split())))
    print(intersec(intervals))
    # for _ in range(100):
    #     print(intersec(test(3, (1, 5, 10))))