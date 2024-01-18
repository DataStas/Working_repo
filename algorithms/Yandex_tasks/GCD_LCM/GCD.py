def gcd_slow(a: int, b: int):
    for d in range(1,  min(a, b)):
        if a % d == 0 and b % d == 0:
            return d


def gcd_better(a: int, b: int):
    while a > 0 and b > 0:
        if a >= b:
            a = a - b
        else:
            b = b - a
    return max(a, b)


# Евклида
def gcd(a: int, b: int):
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def gcd_rec(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd_rec(b, a % b)


if __name__ == '__main__':
    a, b = input().split(' ')
    print(a, b)
    # print(gcd(*(input().split(' '))))