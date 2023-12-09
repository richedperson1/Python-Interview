"""
Generator is special kind of function where we can used yield as the keyword 
"""


def generator():
    print("Hll")
    yield "Hello world"

    print("First function")
    yield("hello world second yield")


# gen = iter(generator())
# print(next(gen))
# print(next(gen))


"""
Multiple time generator called
"""


def generate_num():
    i = 0
    while True:
        yield i**2
        i += 1


square_num_Gen = generate_num()
print(next(square_num_Gen))
print(next(square_num_Gen))
print(next(square_num_Gen))
print(next(square_num_Gen))