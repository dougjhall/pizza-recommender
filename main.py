from data import *
from linkedlist import LinkedList

#outline supported types of pizza
all_pizza_types = ['chicken', 'veggie', 'pepperoni', 'sausage']

#function to load the linked lists
def create_pizza_date():
    pizza_data_list = LinkedList()
    #this ensure that all the pizza with the same types are grouped together
    for type in all_pizza_types:
        pizza_sublist = LinkedList()
        for pizza in pizza_data:
            if pizza[0] == type:
                pizza_sublist.insert_beginning(pizza)
        pizza_data_list.insert_beginning(pizza_sublist)
    return pizza_data_list

all_pizza_data = create_pizza_date()
valid_type = False

#user prompt
while valid_type == False:
    user_input = str(input("What type of pizza would you like? (chicken, veggie, pepperoni, sausage) ")).lower()
    if user_input not in all_pizza_types:
        print("Enter a valid type.")
    else:
        valid_type = True

#loop through linked lists and print the pizzas that match the type the user entered
print("Here are some pizza options you will like!")
pizza_list_head = all_pizza_data.get_head_node()
while pizza_list_head.get_next_node() is not None:
    pizza_sublist_head = pizza_list_head.get_value().get_head_node()
    if pizza_sublist_head.get_value()[0] == user_input:
        while pizza_sublist_head.get_next_node() is not None:
            print(pizza_sublist_head.get_value()[1])
            pizza_sublist_head = pizza_sublist_head.get_next_node()
    pizza_list_head = pizza_list_head.get_next_node()