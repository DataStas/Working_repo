from time import perf_counter


def decorating(fn):
    def inner(*args):      
        start = perf_counter()
        result = fn(*args)
        end = perf_counter()
        elapsed = end - start
        print(result)
        print('elapsed', elapsed)
    return inner


@decorating
def calc_factorial(num):
    if num < 0:
        raise ValueError('Please use a number not smaller than 0')
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product


calc_factorial(4)