# Global Scope: It is the area of the program outside functions, 
# where a global variable is available.

# Global Variable:
#  A global variable is a variable created outside of a function. 
# It can be accessed from different parts of the program, 
# including inside functions for reading.

#Local Scope :
#Local scope is the area inside a function where a local variable can be accessed. 

#Local Variable:
# A local variable is a variable created inside a function. 
# It can normally be accessed only inside that function.




x = 10 #global variable

def test():
    print(x) # ❌ local x hasn't been assigned yet
    x = 20 #local variable

test() #error

