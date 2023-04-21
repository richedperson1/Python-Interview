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
    i = 1
    while True:
        i += 1
        return i


square_num_Gen = generate_num()
print(square_num_Gen)
