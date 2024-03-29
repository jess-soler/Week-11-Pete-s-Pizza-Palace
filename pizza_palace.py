"""
    name: pizza_palace.py
    author: Jessica Soler
    created: 3/28/24
    purpose: point of sale program
"""

#-------------------------------IMPORTS-------------------------------#
# import utils.py
import utils

#---------------------------GLOBAL CONSTANTS-------------------------------#
#--------------------------------LISTS-------------------------------#

# pizza types list (string)
PIZZA_TYPE = [
    "1. Supreme",
    "2. Cheese",
    "3. Pepperoni",
    "4. Veggie",
    "5. Meat Lovers"
]

# size(string) and price(int) are parallel lists
# pizza sizes
PIZZA_SIZE = [
    "1. Small $5",
    "2. Medium $10",
    "3. Large $15",
    "4. Extra Large $20"
] 

# PIZZA_PRICE # (int)
PIZZA_PRICE = [
    5,
    10,
    15,
    20
]

#-------------------------------MAIN-------------------------------#
#TODO: use a main function
def main():
    
    #TODO: from utils.py use title()
    print(utils.title("Welcome to Pete's Pizza Palace!"))
    print("Welcome to our online text based ordering system!")
    
    #get pizza type
    type = get_pizza_type()
    
    #testing pizza type
    #print(f"You chose: {PIZZA_TYPE[type]}")

    #get pizza size
    size = get_pizza_size()
    
    #testing pizza size
    #print(f"You chose: {PIZZA_SIZE[type]}")
    
    # display purchase info
    display_purchase(type, size)

#-------------------------------PIZZA TYPE-------------------------------#
def get_pizza_type():
    
    #use a for loop to display the info in the pizza type list
    for type in PIZZA_TYPE:
        print(type)
    
    #use utils.get_int() to get input from the user    
    type = utils.get_int("What pizza do you want to order?: ")
    
    # TODO: subtract 1 from user input
    type = type - 1
    
    #return the index of the pizza type choice
    return type

#-------------------------------PIZZA SIZE-------------------------------#
def get_pizza_size():
        
    #use a for loop to display the information in the pizza size list
    for size in PIZZA_SIZE:
        print(size)
    
    # TODO: use utils.get_int() to get input from user
    size = utils.get_int("What size of pizza do you want to order?: ")
    
    # TODO: subtract 1 from user input
    size = size - 1
    
    #return the index of the pizza size choice
    return size

#-----------------------------DISPLAY PURCHASE-----------------------------#
def display_purchase(type, size):
    
    #lookup the cost of the pizza in the price list
    print(f"You ordered a number {PIZZA_TYPE[type]} pizza.")
    print(f"Size number {PIZZA_SIZE[size]}")
    
    #calculate the cost of the pizza
    cost = PIZZA_PRICE[size]
    
    #display the completed order
    print(f"Your pizza costs: ${cost}")

#-----------------------------CALL MAIN-----------------------------#
# call the main function
if __name__ == '__main__':
    main()