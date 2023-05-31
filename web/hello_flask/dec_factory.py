from time import perf_counter

# A decorator factory is a function that returns a decorator.
def decorator_factory(loops_num):
    def decorating(fn):
        def inner(num):   
            total_elapsed = 0
            for _ in range(loops_num):
                start = perf_counter()
                result = fn(num)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed/loops_num
            print('result is', result)    
            print('num of loops is', loops_num)
            print('avg time elapsed', avg_run_time)
        return inner
    return decorating


@decorator_factory(500)
def calc_factorial2(num):
    if num < 0:
        raise ValueError('Please use a number not smaller than 0')
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product

calc_factorial2(4)


class Decorator_Factory_Class:
    def __init__(self, num_loops):
        self.num_loops = num_loops
    def __call__(self, fn):
          def inner(num):   
            total_elapsed = 0
            for i in range(self.num_loops):
                start = perf_counter()
                result = fn(num)
                end = perf_counter()
                total_elapsed += end - start
            avg_run_time = total_elapsed/self.num_loops
            print('num of loops is', self.num_loops)
            return result
          return inner
      
      
@Decorator_Factory_Class(5)
def calc_factorial2(num):
    if num < 0:
        raise ValueError('Please use a number not smaller than 0')
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product
calc_factorial2(4)