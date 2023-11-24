# # Functions inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2


# def substrac(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def devide(n1, n2):
#     return n1 / n2

# # python fucntions are know as First-class objects,
# # can be passed around as argumentss e.g. int/float/str


# def calculate(calc_funcction, n1, n2):
#     return calc_funcction(n1, n2)

# res = calculate(multiply, 2, 3)
# print(res)


# # Nested Functions
# def outer_function():
#     print("I'm outer")
    
#     def nested_function(): # declared inside - access inside
#         print("I'm inner")

#     nested_function() # executed

# # nested_function() # dosen't work
# outer_function()


# # Functions can be returned in other functions
# def outer_function():
#     print("I'm outer")
    
#     def nested_function():  # declared inside - access inside
#         print("I'm inner")

#     return nested_function  # () - activator of functions

# inner_fun = outer_function()
# inner_fun()



#  Python Decorator

"""Step 1"""
# def decorator_function(function):
#     def wrapper_function():
#         function() # just call, but we can add functionality
#     return wrapper_function
# import time

"""Step 2"""
# def decorator_function(function):
#     def wrapper_function():
#         function() # just call, but we can add functionality
#     return wrapper_function


# def say_hello():
#     time.sleep(2)
#     print('Hello')


# def say_bye():
#     time.sleep(2)
#     print('Bye')
    
    
# def say_greeting():
#     time.sleep(2)
#     print('How are you')

# say_hello()

"""Step 3"""
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)  # add functionality
        # Do before function
        function()
        # Do after function
    return wrapper_function


@delay_decorator
def say_hello():
    print('Hello')


@delay_decorator 
def say_bye():
    print('Bye')


@delay_decorator # @ syntax suger - makes typing easier
def say_greeting():
    print('How are you')


decor_fun = delay_decorator(say_greeting)  # same as @
decor_fun()