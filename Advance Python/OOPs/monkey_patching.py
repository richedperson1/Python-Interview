

"""
Changing the behavior of the class at the run-time.

also it refer to dynamic (or run-time) modifications of a class or module

As every thing in the python is object, We can change object into any other object
"""


class power:
    def squareFun(self, num):
        return(f"The square of number is {num**2}")


def cube(self, num):
    return(f"The cube of number is {num**3}")


def cube2(self, num):
    return(f"The cube2 of number is {num**3+6}")


"""
At run time we are changing function behaviour we are adding new function in the class 
It happen only in the python
"""
# obj.squareFun = cube
power.squareFun = cube
power.squareCube3 = cube2

obj = power()

# print(obj.squareCube3(2))

"""
Doing monkey patching using object of the class it wouldn't be affect the main class behaviour
"""


def objectFunction(num):
    return "Object function calling "+str(num)


obj1 = power()

obj1.objFun = objectFunction

abc = obj1.objFun(5)
print(abc)

# objfun not availble for another object

obj2 = power()
