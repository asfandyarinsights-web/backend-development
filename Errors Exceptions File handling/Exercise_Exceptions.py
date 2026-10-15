# Out of Index Error
# Starter code
items = [1,2,3,4,5]

try:
    item = items[6]
except IndexError :
    print("Item does not exist in the list")



# Division By Zero Error
# Starter code
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except ZeroDivisionError:
    print("Dividing By Zero Not Allowed")


# FileNotFoundError

# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File Does not exist")