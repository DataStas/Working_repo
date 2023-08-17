import random
from typing import Tuple


def intersec(intervals: list) -> int:
    points = []
    for interval in intervals:
        points.append(list(range(interval[0], interval[1]+1)))
    count = 0
    print(intervals, points)
    for point_set in points:
        for point in point_set:
            points_copy = points.copy()
            points_copy.remove(point_set)
            if point_set not in points_copy:
                count += 1
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