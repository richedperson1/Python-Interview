"""
It method to perform task in the list itself rather than using external function
"""


# Using simple function
def square_numer(lst):

    arr = []
    for ind, data in enumerate(lst):

        arr.append(data**2)

    return arr


arr = [1, 2, 3, 4, 5]

result_for = square_numer(arr)
print(result_for)


# By using list comprehention

arr2 = [i**2 for i in arr]
print(arr2)
