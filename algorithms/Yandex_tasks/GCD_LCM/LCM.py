def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b, a % b)


def lcm(a, b):
    return a*b//gcd(a, b)

if __name__ == '__main__':
    a, b = input().split(' ')
    print(a, b)
    # print(gcd(*(input().split(' '))))