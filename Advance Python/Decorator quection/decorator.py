"""
Hey there! So, a decorator in Python is like a special sticker or a badge that you can put on a 
function or a class to make it do something extra.

It's like having a plain cookie, but then you put some frosting on top to make it sweeter and yummier. 
The decorator does the same thing - it takes a normal function or a class, and adds some extra code to 
it to make it more useful.

For example, you can have a decorator that adds a message before and after a function is called, or a 
decorator that checks if the input to a function is valid before running it. You just need to put the 
decorator's name with an "@" symbol in front of the function or class you want to decorate.

Decorators are a really helpful tool in Python that can make programming more fun and efficient.

"""


"""
Method 1
Implemented decorator 
"""


def decorator(fun):
    ans = fun()
    return ans+", This is made using python"


def simple_de():
    return "Hello world"


# print(decorator(simple_de))


"""
Method 2
Implemented decorator Using @ symbol
"""


def wrapper1(function):
    def decorate_function():
        wrap = function()
        output = ""
        if int(wrap) > 10:
            output = f"Your number : {wrap}, It not need anything else"
        else:
            output = f"Your number : {wrap}, You need to change"

        return output

    return decorate_function


@wrapper1
def first_simple() -> str:
    n = 1
    return int(n * 5)


# print(first_simple()).


""" 
How to give input to the decorator function ? 

=> Following are the answer for the same.
"""


def wrapper(function):
    def decorate_function(a):
        wrap = function(a)
        output = ""
        if int(wrap) > 10:
            output = f"Your number : {wrap}, It not need anything else"
        else:
            output = f"Your number : {wrap}, You need to change"

        return output

    return decorate_function


@wrapper
def function_simple(n: int) -> str:
    return int(n * 5)


# print(function_simple(3))


# Method 3

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function is called.")
        self.func()
        print("After function is called.")


@MyDecorator
def say_hello():
    print("Hello!")


# method 4 Calling decorator method


class MyDecorator2:
    def __init__(self, func):
        self.func = func

    def __call__(self, first):
        print("Before function is called.")
        print(self.render())
        self.func(first)
        print("After function is called.")
        return 0

    def render(self):

        return "Render method called"


@MyDecorator2
def say_hello2(first):
    print("Hello!", first)
    return "First method"


say_hello2("hello")
