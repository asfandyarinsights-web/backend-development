menu=['espresso', 'mocha','latte','cappuccino','cortado','americano']

def find_coffe(coffee):
    if coffee[0] == 'c':
        return coffee
    else:
        return None
filter_item=filter(find_coffe,menu)

# filter () finds the truthy values based on condition 
for item in filter_item:
    print(item)

