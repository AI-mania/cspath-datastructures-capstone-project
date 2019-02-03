from hash_map import HashMap
from linked_list import LinkedList
from data import *

def restaurant_info_generator(restaurant):
  restaurants = HashMap(15)
  german_restaurants = LinkedList(' ')
  japanese_restaurants = LinkedList(' ')
  vegetarian_restaurants = LinkedList(' ')
  french_restaurants = LinkedList(' ')
  african_restaurants = LinkedList(' ')
  american_restaurants = LinkedList(' ')
  barbecue_restaurants = LinkedList(' ')
  czech_restaurants = LinkedList(' ')
  chinese_restaurants = LinkedList(' ')
  thai_restaurants = LinkedList(' ')
  mexican_restaurants = LinkedList(' ')
  indian_restaurants = LinkedList(' ')
  cafe_restaurants = LinkedList(' ')
  pizza_restaurants = LinkedList(' ')
  italian_restaurants = LinkedList(' ')
  
  for food in restaurant_data:
    if food[0] == "german":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      german_restaurants.insert_beginning(restaurant_data_entry)
      
      german_restaurants_string = german_restaurants.stringify_list()
      
    if food[0] == "japanese":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      japanese_restaurants.insert_beginning(restaurant_data_entry)
      
      japanese_restaurants_string = japanese_restaurants.stringify_list()
      
    if food[0] == "vegetarian":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      vegetarian_restaurants.insert_beginning(restaurant_data_entry)
      
      vegetarian_restaurants_string = vegetarian_restaurants.stringify_list()
      
    if food[0] == "french":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      french_restaurants.insert_beginning(restaurant_data_entry)
      
      french_restaurants_string = french_restaurants.stringify_list()
      
    if food[0] == "american":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      american_restaurants.insert_beginning(restaurant_data_entry)
      
      american_restaurants_string = american_restaurants.stringify_list()
      
    if food[0] == "african":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      african_restaurants.insert_beginning(restaurant_data_entry)
      
      african_restaurants_string = african_restaurants.stringify_list()
      
    if food[0] == "barbecue":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      barbecue_restaurants.insert_beginning(restaurant_data_entry)
      
      barbecue_restaurants_string = barbecue_restaurants.stringify_list()
      
    if food[0] == "czech":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      czech_restaurants.insert_beginning(restaurant_data_entry)
      
      czech_restaurants_string = czech_restaurants.stringify_list()
      
    if food[0] == "chinese":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      chinese_restaurants.insert_beginning(restaurant_data_entry)
      
      chinese_restaurants_string = chinese_restaurants.stringify_list()
      
    if food[0] == "thai":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      thai_restaurants.insert_beginning(restaurant_data_entry)
      
      thai_restaurants_string = thai_restaurants.stringify_list()
      
    if food[0] == "mexican":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      mexican_restaurants.insert_beginning(restaurant_data_entry)
      
      mexican_restaurants_string = mexican_restaurants.stringify_list()
      
    if food[0] == "indian":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      indian_restaurants.insert_beginning(restaurant_data_entry)
      
      indian_restaurants_string = indian_restaurants.stringify_list()
      
    if food[0] == "cafe":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      cafe_restaurants.insert_beginning(restaurant_data_entry)
      
      cafe_restaurants_string = cafe_restaurants.stringify_list()
      
    if food[0] == "italian":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      italian_restaurants.insert_beginning(restaurant_data_entry)
      
      italian_restaurants_string = italian_restaurants.stringify_list()
      
    if food[0] == "pizza":
      name = food[1]
      price = food[2]
      rating = food[3]
      address = food[4]
      restaurant_data_entry = """
      Name: {}
      Price: {}
      Rating: {}
      Address: {}
      ---------------------------------""".format(name,price,rating,address)
      pizza_restaurants.insert_beginning(restaurant_data_entry)
      
      pizza_restaurants_string = pizza_restaurants.stringify_list()
        
  restaurants.assign("german", german_restaurants_string)
  restaurants.assign("japanese", japanese_restaurants_string)
  restaurants.assign("vegetarian", vegetarian_restaurants_string)
  restaurants.assign("french", french_restaurants_string)
  restaurants.assign("american", american_restaurants_string)
  restaurants.assign("african", african_restaurants_string)
  restaurants.assign("barbecue", barbecue_restaurants_string)
  restaurants.assign("czech", czech_restaurants_string)
  restaurants.assign("chinese", chinese_restaurants_string)
  restaurants.assign("thai", thai_restaurants_string)
  restaurants.assign("mexican", mexican_restaurants_string)
  restaurants.assign("indian", indian_restaurants_string)
  restaurants.assign("cafe", cafe_restaurants_string)
  restaurants.assign("italian", italian_restaurants_string)
  restaurants.assign("pizza", pizza_restaurants_string)
  
  restaurant_retrieval = restaurants.retrieve(restaurant)
  
  print(restaurant_retrieval)
