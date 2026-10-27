
numbers=[2,4,6,8,10,12,14,16,18,20]

newlist=[num *2 for num in numbers]

print(newlist)


numbers = [2, 4, 6, 8]
# [expression for itemin List]

'''
result=[]
for i in numbers:
    print(i)
    result.append(i+3)
'''
result = [n + 3 for n in numbers]



print(result)

# We want to create a new list containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evenNumber=[]
print("Even Numbers Are...")
# for item in numbers:
#     if item % 2==0:
#         evenNumber.append(item)

evenNumber=[item for item in numbers if item %2==0]

print(evenNumber)



numbers = [1, 2, 3, 4, 5]

result = [item * 10 for item in numbers if item % 2 != 0]
print("ODD Numbers Are...")

print(result)



numbers = [1, 3, 5, 7, 9]

even_numbers = [n for n in numbers if n % 2 == 0]
print('Empty List')
print(even_numbers)


# This filters numbers.
# But what if we want to keep every number and label it "Even" or "Odd"?

numbers = [1, 2, 3, 4, 5]

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result)


numbers = [10, 15, 20, 25]

result = [n * 2 if n > 15 else n for n in numbers]

# [n * 2 for n in numbers if n > 15]
# Numbers that don't satisfy the condition are excluded.

print(result)



numbers = [1, 2, 3, 4, 5, 6]

result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n * 10)
    else:
        result.append(n * 5)

# When using both if and else in list comprehension
# they must appear before the for loop.

result=[n * 10 if n%2==0 else n * 5 for n in numbers ]
print(result)


a = [[96], [69]]

print(''.join(list(map(str, a))))


z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)