# How to provide default values
def my_fun(a=1, b=2, c=3):
    # default values
    print(a, b, c)
    pass


# change one of default
# my_fun(b=3)

# Unlimited Arguments
def add1(n1, n2):
    return n1 + n2


# * - any number of arguments
# unlimited position arguments
# refer by POSITION
def add2(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


# print(add2(1, 2, 3))


# ** - any number of key word arguments
# many keyworded arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    return n


# print(calculate(2, add=3, multiply=5))


class Car:
    
    def __init__(self, **kw):
        self.make = kw['make']
        # self.model = kw['model']
        self.modek = kw.get('model') # benefit if not exists than return None not an error


my_car = Car(make='Nissan', model="GT-R")
print(my_car.model)