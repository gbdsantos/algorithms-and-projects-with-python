def func():
    return 1

func()

def hello(name='Jose'):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is welcome() inside hello'

    def welcome():
        return '\t This welcome() inside hello'

    print("I am going to return a function!")

    if name == 'Jose':
        return greet
    else:
        return welcome()

def cool():

    def super_cool():
        return "I am super very cool"

    return super_cool()

def new_decorator(original_function):

    def wrap_func():

        print('Some extra code, before the original function!')

        original_function()

        print('Some extra code, after the original function!')
    return wrap_func()

@new_decorator
    def func_needs_decorator():
        print("I want to be decorated!")
