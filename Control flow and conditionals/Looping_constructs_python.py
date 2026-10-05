'''
A looping construct refers to the grammatical 
syntax, keywords, and structural rules provided by the language to build a loop.

In Python There Are Two For... and while...

'''
str="Pakistan"

# for items in str:
    # print(items)

favorites=['Cream Brulee','Apple Pie','Churos','Tiramus','Chocolate Cake']

# FOR LOOP
for items in favorites:
    print(items)

print("\n")

# While LOOP
count = 0
while count < len(favorites):
    print(favorites[count])
    count+=1

# Enumerate Function
# Instead of manually managing a counter variable or using range(len(sequence))   
for idx,items in enumerate(favorites):
    print(idx,items)



i = 0
while i<=10:
    print(i)
    i=i+1 


# for i in range (0,4):
#     print(f"looping {i}")
