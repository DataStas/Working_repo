import random


def sum_of_polinoms(k1: int, first: list, k2: int, second: list) -> str:
    first = int(str(first).replace(',', '')[1:-1].replace(' ', ''))
    second = int(str(second).replace(',', '')[1:-1].replace(' ', ''))
    ans = first+second
    ans = [int(x) for x in str(ans)]
    return f'{len(ans)-1}\n' + str(ans).replace(',', '')[1:-1]




def test(k1, k2):
    c1 = [random.randint(1, 9) for _ in range(k1+1)]
    c2 = [random.randint(1, 9) for _ in range(k2+1)]
    return k1, c1, k2, c2



if __name__ == '__main__':
    # k1 = int(input())
    # c1 = [*map(int, input().split())]
    # k2 = int(input())
    # c2 = [*map(int, input().split())]
    test_1 = test(1, 9)
    print(test_1)
    print(sum_of_polinoms(*test_1))
    # with open('output.txt', 'w') as f:
    #     f.write(sum_of_polinoms(*test_1))