#Polymorphism

# In Python, this specific type of polymorphism is known as
# Operator Overloading.

string = "poly"
num = 7
sequence = [1,2,3]


new_str = string * 3
# With Strings (string * 3): It performs text repetition.
# It takes "poly" and glues it together three times to make "polypolypoly".


new_num = 7 * 3
# With Numbers (num * 3): It performs traditional arithmetic multiplication.
# It calculates (7 * 3) and returns 21.


new_sequence = sequence * 3
# With Lists/Sequences (sequence * 3): It performs sequence duplication. 
# It duplicates the items inside the list, returning [1, 2, 3, 1, 2, 3, 1, 2, 3].

print(new_str, new_num, new_sequence)
    


string = "poly"
sequence = [1,2,3]

print(len(string))
# For the string "poly", it returns 4 because there are 4 characters in the string.

print(len(sequence))
# For the list [1, 2, 3], it returns 3 because there are 3 elements in the list.