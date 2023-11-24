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


def PisanoPeriod(m: int):
    current = 0
    next = 1
    period = 0
    while True:
        oldNext = next
        next = (current + next) % m
        current = oldNext
        period = period + 1
        if current == 0 and next == 1:
            return period


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


# Calculate Fn mod m
def fibonacciModulo(n, m=10):
    if n <= 1:
        return n
    # Getting the period
    pisano_period = pisanoPeriod(m)
    # Taking mod of N with
    # period length
    n = n % pisano_period
    previous, current = 0, 1
    for i in range(n-1):
        previous, current = current, previous + current
    return current % m


@time_calc
def test(min: int, max: int, test_num: int):
    cur_test = 0
    while cur_test < test_num:
        a_test = random.randint(min, max)
        n = fibonacciModulo(a_test)
        print(f'Current ans for {a_test}: {n}')
        cur_test += 1


if __name__ == '__main__':
    print((fibonacciModulo(int(input())+2, 10) - 1 + 10) % 10)