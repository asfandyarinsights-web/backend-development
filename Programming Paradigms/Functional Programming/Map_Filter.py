# Without Map function

myList =[2,3,4,5]

newList=[]

for i in myList:
    newList.append(i*2)

print(newList)

# With Map function

def double(n):
    return n*2

result=map(double,myList)
'''
One important detail: map() returns a map object (an iterator),
not a list directly.
That's why we use list(result) to see all the results as a list.
'''

print(list(result))



menu=['espresso', 'mocha','latte','cappuccino','cortado','americano']

def find_coffe(coffee):
    if coffee[0] == 'c':
        return coffee
    else:
        return 'NA'

map_coffee=list(map(find_coffe,menu))
print(map_coffee)


'''
Your intention seems to be finding only the coffee names starting with 'c'.
map() transforms every element,
whereas filter() selects elements based on a condition.
'''

fileted_coffee=list(filter(find_coffe,menu))
print(fileted_coffee)
