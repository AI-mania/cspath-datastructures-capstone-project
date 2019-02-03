from data import *
from welcome import *
from hash_map import HashMap
from linked_list import LinkedList
from restaurant_info_generator import *



def project_engine():
  food_types = LinkedList()
  for food in types:
    food_types.insert_beginning(food)
  food_types = food_types.stringify_list()
  list_food_types = food_types.split("\n")
  del list_food_types[-1]
  user_food_types = LinkedList()
  if len(user_input) == 1:
    for food in list_food_types:
      if user_input == food[0]:
        user_food_types.insert_beginning(food)       
  if len(user_input) > 1:
    for food in list_food_types:
      if user_input in food:
        user_food_types.insert_beginning(food)
              
  current_node = user_food_types.get_head_node()
  user_food_list = []
  while current_node.get_value():
    user_food_list.append(current_node.get_value())    
    current_node = current_node.get_next_node()
  if len(user_food_list) == 0:
    print("No restaurants begin with that letter. Type in more than one letter for more accurate results.")
  elif len(user_food_list) > 1:
    print("With those beginning letters, your choices are {0}.".format(user_food_list))
    
  else:
    restaurant = user_food_list[0]
    print("The only option with those beginning letters is {0}\nDo you want to look at {0} restaurants?".format(restaurant))
    restaurant_input = str(input("Enter 'y' for yes and 'n' for no\n"))
    if restaurant_input == 'n':
      pass
    elif restaurant_input == 'y':
      restaurant_info_generator(restaurant)
      more_restaurant_input = str(input("Do you want to find other restaurants? Enter 'y' for yes and 'n' for no"))
      if more_restaurant_input == 'y':
        pass
      elif more_restaurant_input == 'n':
        exit(0)
      else:
        print("Invalid input. Next time enter 'y' for yes and 'n' for no.")
      
    else:
      print("Invalid input. Next time enter 'y' for yes and 'n' for no")
  
  
      

while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType that food type or the beginning of that food type and press enter to see if it's here.\n")).lower()
    
    project_engine()





    
