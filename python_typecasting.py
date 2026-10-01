'''
A company wants to determine the general age of its customers. 
You help them by writing a program that uses a customer's ID number (7512171283423)
to determine his or her age. 
But the data set that you are provided with has the ID numbers saved as strings. 
Answer ==
int('7512171283423')

# Implicit Type Casting

num_int = 10    # Integer type
num_flo = 5.5   # Float type

# Python automatically converts num_int to a float before adding
result = num_int + num_flo

print(result)        # Output: 15.5
print(type(result))  # Output: <class 'float'>


# Explicit Type Casting

# Converting a string to an integer (useful for user inputs)
age_str = "25"
age_int = int(age_str) 

# Converting a float to an integer (causes data loss by stripping decimals)
pi = 3.14
pi_int = int(pi) 

print(age_int + 5)  # Output: 30
print(pi_int)       # Output: 3 (the .14 is lost)


'''

# Example

num_1 = input('First number is: ')  #the entered number is still string
num_2 = input('Second number is: ') #the entered number is still string

user_sum = float(num_1) + float(num_2) #temporary float for results
# print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum) # this will cause error

# Recommend Use F Stirng

print(f"The sum of : {num_1} and {num_2} is = {user_sum}") # this will cause error
