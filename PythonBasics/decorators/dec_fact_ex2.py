"""Make a decorator factory which returns a decorator that decorates functions with one argument. 
The factory should take one argument, a type,
and then returns a decorator that makes function should check if the input is the correct type. 
If it is wrong, it should print("Bad Type") (In reality,
it should raise an error, but error raising isn't in this tutorial). 
Using isinstance(object, type_of_object) or type(object) might help."""

# A decorator factory is a function that returns a decorator.
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

# @type_check(str)
# def first_letter(word):
#     return word[0]

# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])
