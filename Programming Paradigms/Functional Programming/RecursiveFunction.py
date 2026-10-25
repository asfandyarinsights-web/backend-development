# Recursive Function
def countDown(n):
    if n==0:
        return

    print(n)

    countDown(n-1)

countDown(5)

print('-----------------------------------')

# Iteration Function

def count_iterative(n):
    while n > 0:
        print(n)
        n -= 1

count_iterative(5)



def printNum(n):
    # This is our base case, or stopping condition.
    if n > 10:  # When to stop
        return

    print(n)  # Do the work

    # This prints the current number.
    # If n = 1, it prints 1. If n = 2, it prints 2, and so on.

    printNum(n+1) # Call itself with the next number
    # here the n-1 goes to negative numbers (RecursionError)

    # This is the recursive call: 
    # the function calls itself again, but this time with the next number.

printNum(1)