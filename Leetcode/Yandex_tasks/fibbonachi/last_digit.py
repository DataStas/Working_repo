import random
from datetime import datetime


def time_calc(fun):
    def wrapper(*args):
        t1 = datetime.now()
        ans = fun(*args)
        t2 = datetime.now()
        print(f'Time for calc {(t1-t2).microseconds}')
        return ans
    return wrapper


def FibonacciLastDigit(n: int):
    if n <= 1:
        return n
    f_nums = [0, 1]
    for ind in range(2, n+1):
        f_nums.append(f_nums[ind-1] + f_nums[ind-2] % 10)
    return f_nums[n]


@time_calc
def test(min: int, max: int, test_num: int):
    cur_test = 0
    while cur_test < test_num:
        a_test = random.randint(min, max)
        n = FibonacciLastDigit(a_test)
        print(f'Current ans for {a_test}: {n}')
        cur_test += 1


if __name__ == '__main__':
    # answers = {}
    # test(50, 100, 1000)
    print(FibonacciLastDigit(int(input())))