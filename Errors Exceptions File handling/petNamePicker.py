import random

try:
    with open('Errors Exceptions File handling/petNames.txt','r') as file:
        petnames=file.read()

        petnames_list=petnames.split("\n")

        random_pet=random.choice(petnames_list)

        print(f'List OF Pets: {petnames_list}')
        
        print(f'My Chosen Pet Is : {random_pet}')

except FileNotFoundError:
    print("File Not Found")