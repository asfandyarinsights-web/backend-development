studentData = {
    "name": "Asfandyar",

    "marks": [80, 85, 90],

    "age":21,
    
    "active": True,
    
    "address": {
        "city": "Nawabshah",
        "country": "Pakistan"
    }
}

print(studentData["marks"])
print(studentData["address"]["city"])

# Values And Keys
print(studentData.values())
print(studentData.keys())
print(studentData.items())


# 7. Looping through a dictionary
# Suppose you want to display all student details.

for value in studentData.values():
    print(value)



# Loop through keys and values
# This is particularly useful in real programs.

for key, value in studentData.items():
    print(key," : ",value)
# Here, .items() provides each key-value pair, which Python unpacks into key and value.



'''
8. Useful dictionary methods
Method	    Purpose
get(key)	Retrieve a value safely

keys()	    Get the dictionary's keys

values()	Get its values

items()	    Get key-value pairs

update()	Add or update multiple entries

pop(key)	Remove a key and return its value

clear()	    Remove all entries

copy()	    Create a shallow copy

'''

# Example of update():

studentData.update(
    {
        'age':23,
        'city':"Nawabshah"
    }
)

# The age is updated, and the city is added.
print(studentData)