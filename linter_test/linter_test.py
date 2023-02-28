
from math import sqrt
"""
from math import *
import itertools

def  CalculateSquareRoot (Number ):
    return  sqrt(Number )

def append_item(item, l=[]):
    l.append(item)
    return l

while True:
    try:
        your_number=float(input('Enter your number: '))
        print("Square root is:", CalculateSquareRoot(your_number))
        break
    except:
        pass
"""

def CalculateSquareRoot(Number):
    return sqrt(Number)


def append_item(item):
    test_list = []
    test_list.append(item)
    return test_list


while True:
    try:
        your_number = float(input('Enter your number: '))
        print("Square root is:", CalculateSquareRoot(your_number))
        break
    except your_number < 0:
        print("You have a problem")
    pass

