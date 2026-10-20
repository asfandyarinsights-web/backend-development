try:
    with open('Errors Exceptions File handling/Newtestfile.txt',mode='w') as file:
        file.writelines(["Han Bhai Ban Gyee File Teri","\nYeh Uss File Ki Dosri Line He"])
except FileNotFoundError as e:
    print("File Is Not Found",e)


with open('Errors Exceptions File handling/Newtestfile.txt','r') as file:
    data=file.readlines()
    print(data)