# Define class MyFirstClass
class MyFirstClass:

    def __init__(self):
        print("Who wrote this?")  # Move the print statement into the constructor
    
    
    # Define string variable called index
    index="Author-Book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(F'{philosopher} wrote the book: {book}')

    
    
        

# Call function handlist()
whodunnit=MyFirstClass()

whodunnit.hand_list("Plato","Republic")

whodunnit.hand_list("Sun Tzu","Are Of War")
