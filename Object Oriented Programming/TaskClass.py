# Define class MyFirstClass
class MyFirstClass:
    print('Who Wrote this')

    # Define string variable called index
    index="Author-Book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print(F'{philosopher} wrote the book: {book}')

    
    
        

# Call function handlist()
whodunnit=MyFirstClass()

whodunnit.hand_list("Plato","Republic")

whodunnit.hand_list("Sun Tzu","Are Of War")
