class MyClass:
    a=5

    def hello(self):
        print('Hello World')

object_class=MyClass()

# print(MyClass.hello())
print(object_class.hello())

print(MyClass.a)
'''
1. Direct Access: 
(MyClass.a)
When you call MyClass.a, 
you are going straight to the blueprint (MyClass) and asking for its variable a.
It looks inside itself, finds 5, and prints it.
'''


print(object_class.a)

'''

2. The Chain of Command Lookup: (object_class.a)
When you call object_class.a, Python uses a specific lookup order:

1. First, it looks inside the specific instance (object_class) to see if it has a unique, personal variable named a.

2. It doesn't find one, because you didn't create an instance variable (like self.a = 5 inside an __init__ function).

3. Instead of giving up, Python automatically looks up the chain to the parent class (MyClass) to see if the class has an a.
'''


class OtherClass:
    a = 5


obj1 = OtherClass()
obj2 = OtherClass()

# Case A: Changing it via the Class affects everyone
OtherClass.a = 10
print(obj1.a)  # Prints 10 (because it still looks up to the class)
print(obj2.a)  # Prints 10

# Case B: Changing it via an Object isolates the change
obj1.a = 99  # This creates a brand-new, personal variable 'a' ONLY inside obj1
print(obj1.a)  # Prints 99 (found inside the object)
print(obj2.a)  # Prints 10 (still looking up to the class)
print(OtherClass.a)  # Prints 10 (the class blueprint remains unchanged)


