class Student:

    def __init__(arguments,name, age):
        arguments.name = name
        arguments.age = age


student1 = Student('AsfandYar Chandio',22)
student2 = Student('Muhammed Salim',54)



print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)







'''
4. One important programming insight
Think about a real backend application.

Suppose you're creating 1,000 user accounts.
Without __init__, you would have to create objects and manually assign their attributes.
With __init__, you can initialize each user consistently when creating the object.
That's why __init__ is commonly used in object-oriented programming.
'''






class Student:

    def __new__(cls):

        print("Creating student object")

        # This is the actual object creation.
        obj = super().__new__(cls)

        return obj


    def __init__(self):
        print("Initializing student")


student1 = Student()


class Laptop:

    def __new__(cls,name):
        print("Creating Laptop object :" ,name)

        obj=super().__new__(cls)
        return obj
    
    def __init__(self,name):
        self.name=name
        print("Initializing object : ",name)


laptop1 = Laptop('HP')
