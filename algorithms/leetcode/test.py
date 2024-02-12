from time import sleep
from time import time_ns


def dec(fun_c_to_dec: callable):
    local_vars = {}

    def wrapper(*args, **kwargs):
        print('Dec_in')
        t = time_ns()
        fun_c_to_dec(args[0], *args, **kwargs)
        print('Dec_out')
        print(t-time_ns())

    return wrapper


@dec
def fun(a: str, *args, **kwargs):
    print('Fun_in')
    print(a)
    print(args)
    print(kwargs)
    sleep(1)
    print('Fun_out')

if __name__ == '__main__':
    print(fun('string', 1, 2, 10, d=15))