'''
Lesson 2: What is *args?
*args allows a function to accept any number of positional arguments.

'''
def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30)


'''
Notice something important: Python collects the values into a tuple.
A tuple is a collection of values, similar to a list,
but it is immutable (you cannot change its elements).
'''


'''
One small but important detail: args is not a special Python keyword.
The special part is the *. You could call it *numbers, *values, or *students.
However, *args is the standard convention.
'''

# Printing the tuple is fine, but what if we want to add all the numbers?

def add_numbers(*args):
    total=sum(args)
    print(f"Sum Of Numbers Is {total}")

add_numbers(10, 20, 30)
add_numbers(2, 5, 1)
add_numbers(10, 20, 30,54,32)


'''
Lesson 4: Loop through *args
Since args is a tuple, you can loop through it just like a list.
'''
def show_marks(*args):
    for mark in args:
        print(mark)

show_marks(75, 85, 90, 68)


# You can even calculate an average:

def calculateAverage(*args):
    if not args:  
        #if not args check. If the user calls average_marks() without any marks
        # dividing by len(args) would cause a ZeroDivisionError. The if not check prevents that.
        print("No Marks Provided")
        return
    average=sum(args)/len(args)
    print(f"Average : {average}")

calculateAverage(10,20,39)




'''
Lesson 5: What is **kwargs?
**kwargs allows a function to accept any number of keyword arguments.
function call : student(name="Asfand", age=21)

'''

# Lesson 6: Loop through **kwargs

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name = "Asfand", age = 21, department = "IT", city = "Karachi")


# For example, you could use this idea to display 
# user profiles, 
# print product details,
# or process configuration settings.


# Lesson 7: Use both together
# You can use *args and **kwargs in the same function.

def show_data(*args, **kwargs):
    print("Positional data:", args)  #10, 20, 30 go into the tuple args.
    print("Keyword data:", kwargs)  #name="Asfand" and city="Karachi" go into the dictionary kwargs

show_data(10, 20, 30, name="Asfand", city="Karachi")



# Lesson 8: The most important advanced trick — unpacking
# But these symbols can also do the opposite: 
# unpack a collection and pass its contents as arguments.



# A. Unpacking a list with *
numbers = [10, 20, 30]

def add(a, b, c):
    print(a + b + c)

add(*numbers) # equivalent to add(10, 20, 30)
# The * takes the elements out of the list
# and passes them as separate positional arguments.


# B. Unpacking a dictionary with **

student = {
    "name": "Asfand",
    "age": 21
}

def show_student(name, age):
    print(f"{name} is {age} years old.")

show_student(**student)


# Lesson 9: Parameter order rules
# Python has rules about where parameters must appear in a function definition.

def student_info(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

student_info("Asfand", 75, 85, 90, city="Karachi",department="IT")

'''
The general order is:
1. Regular parameters.
2. *args, if needed.
3. Keyword-only parameters, if any.
4. **kwargs, if needed.

'''


# Lesson 10: Keyword-only arguments
# Sometimes you want a parameter to be supplied by name,
# rather than accidentally by position.

def create_account(name, *, is_admin=False):
    print(name)
    print(is_admin)

create_account("Asfand", is_admin=True)
# The standalone * marks the boundary: parameters after it must be supplied by keyword.

# create_account("Asfand", True) But this call fails:

# This is helpful when a function has settings such 
# as is_admin, reverse, debug, or save_file.
# Naming the setting makes the call clearer and reduces accidental mistakes.



# Lesson 11: A real-world example — flexible student records

# Imagine you're making a student record system.
# Every student has a name, but their other details may differ.

def create_student(name, *marks, **details):
    print(f"Student: {name}")

    if marks:
        average = sum(marks) / len(marks)
        print(f"Average marks: {average:.2f}")
    else:
        print("No marks provided")

    print("Additional details:")

    for key, value in details.items():
        print(f"{key}: {value}")

create_student("Asfand", 75, 85, 90, city="Karachi",department="IT", semester=6)


# Lesson 12: Advanced use — forwarding arguments
# One powerful use of *args and **kwargs is forwarding arguments from one function to another.

def greet(name, city):
    print(f"Hello {name} from {city}!")


def wrapper(*args, **kwargs):
    greet(*args, **kwargs)


wrapper("Asfand", city="Karachi")

'''
The wrapper() function doesn't need to know the exact parameters of greet(). 
It accepts the arguments and forwards them.
This technique is used in 
decorators,
logging utilities,
testing helpers,
and framework code.
'''