class Recipe():

    def __init__(self,dish,items,time):
        self.dish=dish
        self.items=items
        self.time=time

    def contents(self):
        print(f"The {str(self.dish)} has {str(self.items)} and take {str(self.time)} min to prepare")

pizza=Recipe("Pizza",['cheese','bread','tomato'],45)
pasta=Recipe("Pasta",['penne','sauce'],55)

print(f"item name is : {pizza.dish}")
print(f"item ingredient are : {pizza.items}")
print(f"item time to prepare  is : {pizza.time}")

print(pasta.items)

print(pizza.contents())
print(pasta.contents())