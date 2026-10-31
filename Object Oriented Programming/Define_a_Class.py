class House:
   
    '''
    This is a stub for a class representing a house that can be 
    used to create objects and evaluate different metrics
    that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(argument,rate):
        print(argument.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost

house = House()


# changing the atribute of object
house.num_rooms=7

House.num_rooms=8

# Object Instantiated
print(house.num_rooms)

# Direct Class Call
print(House.num_rooms)





