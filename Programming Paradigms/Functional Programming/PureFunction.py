# Not Pure Function
global_list=[1,2,3]

# def add_to(item):
#     newlist=global_list.copy()
#     newlist.append(item)
#     return global_list.append(item)

# add_to(4)

# print(global_list)


# Pure Function

def add_to_list(item):
    newlist=global_list.copy()
    newlist.append(item)
    return newlist 


print(global_list)
print(add_to_list(7))
# print(global_list)
