try:
    with open('Errors Exceptions File handling/sample.txt','r') as file:
        # data=file.read(40) #read whole file at once
        # line1=file.readline() # read line by line
        # line2=file.readline() # read line by line
        # line3=file.readline() # read line by line
        linelist=file.readlines()

        for data in linelist:
            print(data)
        # print(line2)
        # print(line3)



except FileNotFoundError:
    print("File Not Found")
