'''
list comprehension easy way to create new a list
'''
nums=[1,2,3,4,5,6,7,8,9,10]

# i want a 'n' for each 'n' in nums
# # For Loop
# myList=[]
# for i in nums:
#     myList.append(i)


myList=[n for n in nums]
print(myList)


