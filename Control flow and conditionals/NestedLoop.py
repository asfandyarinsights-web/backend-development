# Outer Loop: Run One Time Each For Inner Loop 

for i in range(2):

    # Inner Loop: Runs 10 time then go back to outer loop and this cycle repeats
    for j in range(10):
        print(0,end=" ")
    print()

'''
Outer loop = rows/groups
Inner loop = things inside each row/group
'''

# Simple real-life example
# Imagine a classroom with 3 students, and each student has 2 books.

for student in range(1,4):
    for book in range(1,3):
        print("Student",student,"Book",book)

# Time Complexity Issue Must BE COnsidered
