
# file=open("Errors Exceptions File handling/test.txt", mode='r')

with open("Errors Exceptions File handling/test.txt", mode='r') as file:
    data=file.readline()
    print(data)
