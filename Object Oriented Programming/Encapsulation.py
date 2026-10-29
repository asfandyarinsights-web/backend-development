# Encapsulation
class Alpha:
    
    def __init__(self): #This is a special setup function (called a constructor). 
        
        self._a = 2.  # Protected member ‘a’
        # This creates a variable named _a inside the object and sets it to 2.0.

        self.__b = 2.  # Private member ‘b’
        # This creates a variable named __b and sets it to 2.0.


        print(self._a)
        print(self.__b)

# self._a is a protected member and can be accessed by the class and its subclasses.

# 1. This builds a real object using the Alpha blueprint
my_object = Alpha()


# 2. You can easily look at the "protected" variable:
print(my_object._a)  # Prints: 2.0



# 3. If you try to look at the "private" variable, Python crashes!
# print(my_object.__b)  # ERROR! Python hid it.


# 1. The Right Way: Public Methods (Getters)

class Alpha:

    def __init__(self):
        self._a = 2.0  # Protected
        self.__b = 2.0  # Private

    # This is a public method (anyone can call it)
    def get_private_b(self):
        return self.__b  # It has internal access to __b


# Testing it out:
obj = Alpha()
print(obj.get_private_b())  # Prints: 2.0

'''
Why do this? It's like a bank teller. '
'You aren't allowed to walk into the vault yourself, 
but you can ask the teller (the public method) to go get your money for you.
'''


class Alpha:

    def __init__(self):
        self._a = 2.0  # Protected
        self.__b = 2.0  # Private (Python renames this to _Alpha__b)


obj = Alpha()

# Trying to access it normally fails:
# print(obj.__b) # Error: 'Alpha' object has no attribute '__b'

# Accessing it using Name Mangling works!
print(obj._Alpha__b)  # Prints: 2.0
