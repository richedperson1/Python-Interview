

"""
Key to the python dictionary should be unique and hashble return value

1. Hash return value mean ?
=> It's the value which given by hash function.

2.what is hash function ?
=> It's function which will convert arbitory data size into the fixed data size. It has unique value


So list cann't be key to dictionary

Those
"""

# Tuple is hashble which mean it can used as key to dictionary
dist = {}
tupple = (3, 2, 3)
print(hash(tupple))
dist[tupple] = 5
print(dist)

"""
Tuple will be hashable if tuple element itself is hashable 
Ex. if Tuple contain any data type which has modified after change then it was not hashable

a = tuple([1,2,3])

"a" has hash function return value 

b = tuple([[1,2,3],4])
"b" not be hash function return value
"""

# Dictionary can't be hashable so can't used as key to the dictionary itself
dictionary = {"Rutvik": "jaiswal"}

dist[dictionary] = 12
print(dist)
