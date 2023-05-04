"""
Set vs Frozenset

"""


"""
Similarity

1. It contain only unique value
2. Lookuptime is O(1)
3. Iterable object
"""


"""
desimilarity

1. Immutability : Frozenset is immutable
2. Hashing availble for frozenset as it fixed size
"""


# Frozen set can be used as Dictionary keys
dist = {}
arr = [1, 2, 3, 4, 4]
FrozeArr = frozenset(arr)

dist[FrozeArr] = 5
print(dist)
