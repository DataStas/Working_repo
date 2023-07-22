import random
from datetime import datetime
import time

def time_calc(fun):
    def wrapper(*args):
        t1 = datetime.now()
        ans = fun(*args)
        t2 = datetime.now()
        print(f'Time for calc {(t1-t2).microseconds}')
        return ans
    return wrapper


def fast_fibonacci(fun):
    answers = {}
    def wrapper(n: int):
        t1 = datetime.now()
        if n in answers:
            t2 = datetime.now()
            print(f'Fast solving')
            # print(f'Time for calc {(t1-t2).microseconds}')
            return answers[n]
        else:
            ans = fun(n)
            answers[n] = ans
            t2 = datetime.now()
            # print(f'Time for calc {(t1-t2).microseconds}')
            return ans
    return wrapper


@fast_fibonacci
def Fibonacci(n: int):
    # time.sleep(0.1)
    if n <= 1:
        return n
    prev = 0
    current = 1
    for _ in range(n-1):
        old_prev = prev
        prev = current
        current = old_prev + prev
    return current

@time_calc
def test(min: int, max: int, test_num: int):
    cur_test = 0
    while cur_test < test_num:
        a_test = random.randint(min, max)
        n = Fibonacci(a_test)
        print(f'Current ans for {a_test}: {n}')
        cur_test += 1


if __name__ == '__main__':
    # answers = {}
    # test(50, 100, 1000)
    print(globals())
    print(Fibonacci(int(input())))