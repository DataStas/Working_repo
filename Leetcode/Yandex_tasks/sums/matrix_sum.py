from functools import reduce


def matrix(s1: int, s2: int, first: list, second: list) -> str:

    first = reduce(lambda x, y: x+y, first)
    second = reduce(lambda x, y: x+y, second)
    for ind, n2 in enumerate(second):
        first[ind] += n2
    out = ''
    for ind, n1 in enumerate(first):
        if ind % s2 == 0:
            out += '\n'
        out += f'{n1} '
    return out


if __name__ == '__main__':
    s1, s2 = map(int, input().split())
    m1 = [[*map(int, input().split())] for _ in range(s1)]
    m2 = [[*map(int, input().split())] for _ in range(s1)]
    print(m1, m2)
    print(matrix(s1, s2, m1, m2))