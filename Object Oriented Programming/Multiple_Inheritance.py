# Multiple Inheritance.
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)


# Multi-level inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)




# Built-in functions
# issubclass()

# isinstance().  that determines if some object is an instance of some class.


print(issubclass(A,B)) 
print(issubclass(B,A)) # Is B subclass of A?


class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))





'''
The super() function is a built-in function that can be called inside the Child CLass
and gives access to the methods and variables of the Parent classes or sibling classes.
Sibling classes are the classes that share the same Parent class.
When you call the super() function, 
you get an object that represents the parent class in return.

The super() function allows a child class to call methods from its parent class.
This lets you extend parent functionality rather than completely replace it.
'''


class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()