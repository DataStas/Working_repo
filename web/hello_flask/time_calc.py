import time


def time_measure(func_to_estimate):
    def calc_time():
        time_before = time.time()
        func_to_estimate()
        time_after = time.time()
        return time_after-time_before
    return calc_time

@time_measure
def speed_calc_decorator():
    pass


@time_measure
def fast_function():
    for i in range(10000000):
        i * i


@time_measure
def slow_function():
    for i in range(100000000):
        i * i


time_1 = speed_calc_decorator()
print(time_1)
time_2 = fast_function()
print(time_2)
time_3 = slow_function()
print(time_3)