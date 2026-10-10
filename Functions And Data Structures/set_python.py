'''
In Python, a set is a collection of unique items.
It automatically removes duplicate values.
'''

set_a={1,2,3,4,5}

set_a.add(6)
print(set_a)

# remove() deletes an item, but raises an error if it doesn't exist.
set_a.remove(2)
print(set_a)

# discard() does not raise an error if the item is missing.
set_a.discard(2)
print(set_a)

# 4. Checking whether an item exists
languages = {"Python", "Java", "JavaScript"}

print("Python" in languages)
print("PHP" in languages)


# 5. Set operations

# Union (|)
# Combines items from both sets, without duplicates.
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Intersection (&)
# Finds items shared by both sets(common or same in both sets).
print(a & b)

# Difference (-)
# Finds items in the first set but not the second.

print(a - b)

# Symmetrical Difference (-)
# all of the elements present in set a or set b but not in both sets

print(a ^ b)

# How do you create an empty set?
set_b=set()


'''
6. Important rules to remember
- Sets cannot contain duplicate items.

- Sets do not support indexing or slicing (its un ordered items collection).

- Sets are mutable, meaning you can add or remove items.

- Set elements must be hashable; numbers, strings, and tuples of hashable values are common examples.

- An empty set is created with set(), not {}, because {} creates an empty dictionary.

'''