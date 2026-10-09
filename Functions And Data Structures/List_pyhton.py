List1=[1 , 2 , 3 , 4 , 5]

List2=['A' , 'B' , 'C']

List3=['Hello' , 1 , True , 40.22]

List4=[1, [5,6,3],8]

# add item to list
print(*List1)
print(List1, sep=" ")

List1.insert(len(List1) , 6)
List1.append(7)
List1.extend([6,7,8,9])

print(List1, sep=" ")

# Remove item

popped_item=List1.pop(4)
print("Removed Item Is :",popped_item)
del List1[5]
print(List1, sep=" ")


# Iterate Through a List
for items in List1:
    print(items)



'''
1. What is list slicing?
Definition: List slicing is a way to extract a portion of a list 
by specifying a range of indexes.
'''

# Example A: Get the first three items

students = ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal"]

print(students[0:3])


# Example B: Get items from index 2 to the end

print(students[2:])

# Example C: Get items from the beginning up to index 3

print(students[:3])


# Example D: Select every second item

print(students[::2])

# Example E: Reverse a list

print(students[::-1])
#NOTE: 
#Slicing creates a new list. 
#It does not remove items from or change the original list.


# 1. Membership: the 'in' operator

resources = ["Python Notes", "HTML Notes", "CSS Notes"]

print("HTML Notes" in resources)
print("Java Notes" in resources)

# The 'not in' operator

print("Java Notes" not in resources)

# This is useful for checking whether a value is missing before adding it.

if "JAVA Notes" not in resources:
    resources.append("JAVA Notes")

print(resources)



# 2 : Searching with a loop
marks = [45, 80, 35, 90, 60]

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")



# 3. List comprehensions
'''
A list comprehension is a concise way to create a new list 
by applying an expression to items from an iterable,
optionally filtering which items are included.
'''


#Concept: Suppose you have marks and 
# want to create another list containing only marks of 50 or above.

marks = [45, 80, 35, 90, 60]

passing_marks = [mark for mark in marks if mark >= 50]

print(passing_marks)


'''
1
mark — expression
The value to put into the new list.

2
for mark in marks — iteration
Take each item from the original list, one at a time.

3
if mark >= 50 — condition
Include only items that satisfy the condition.
'''


# doubling numbers

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)