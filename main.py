#  LISTS

# bicycles = ['trek', 'bmx', 'cannondile', 'redline']
# print(bicycles)

# ACCESSING Elements in a List


# bicycles = ['trek', 'bmx', 'cannondile', 'redline']

# print(bicycles[0])
# print(bicycles[0].title())

# print(bicycles[1].title())
# print(bicycles[3].title())

# print(bicycles[-1])
# print(bicycles[-1].title())

#  the index -1 returns the last item in a list. therefore -2, -3 return the second to last and the third to last item in a list, corespondently

#  3. Using individual Values from a list

# bicycles = ['trek', 'bmx', 'cannondile', 'redline']
# message = f"My first bicycle was a {bicycles[1].title()}."
# print(message)

# jobs = ['wagamama', 'cosy cottage', 'dirty blonde', 'watches and crystals']
# message = f"My first job in Brighton was at {jobs[1].title()}, followed by {jobs[0].title()}. Now I am working at {jobs[-1].title()}!"
# print(message)

# Changing, Adding, and Removing Elements

# a) Modifying

# motorcycles = ['honda', 'yamaha', 'suzuki']
# # print(motorcycles[0].title())
# # print(motorcycles)

# motorcycles[0] = 'docati'
# print(motorcycles)

# b) Adding:
#  - by addind append


# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)

# ==================

# motorcycles = []

# motorcycles.append('yamaha')
# motorcycles.append('honda')
# motorcycles.append('suzuki')
# motorcycles.append('ducati')
# print(motorcycles)

#  - by inserting elements into a list

# motorcycles = ['honda', 'yamaha', 'suzuki']
# # motorcycles.insert(0, 'ducati')
# # print(motorcycles)

# motorcycles.insert(2,'lada')
# print(motorcycles)

# c) Removing Elements from a List

# ~ by del Statement {once removed you can no longer access the value of the item that was removed after del statement is used}

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# # del motorcycles[0]
# # print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

# ~ by pop() method {this is used when you want to still access the value of removed item. in a web application for example , you might want to remove a user from a list of active memebers and add that user to a list of inactive members }

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle) 
#  we pop a a value from the list and store that value in the variable pop_motorcycle. once we print the popped value to prove we still have access to that value. 

# motorcycles = ['honda', 'yamaha', 'suzuki']

# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# x = ['a', 'b', 'c']
# triangle_base = x.pop()
# print(f"The longest side of a triangle is the hypothenusis which is {triangle_base}.")

#  ~ Popping Items from any position in a list

# motorcycles = ['honda', 'yamaha', 'suzuki']

# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was {first_owned.title()}.")

#  ~ Removing an Item by Value

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\n\tA {too_expensive.title()} is too expensive for me.")

#  ==> After defining the list, we assign a value 'ducati' to a variable too_expensive. We then use this variable to tell Python which value to remove from the list. Then 'ducati' is removed from the list , but it is still accesible through the variable too expensive, allowing us to write a statement to why we removed 'ducati' from the list of motorcycles. 

#  !  The remove() method deletes only the first occurance of the value you specify. If the value appears more than once in a list, you will need to use a loop to make sure all the occurances of that value have been removed. You will learn how to do that later. 


#  EXERCISES

# guests = ['stella', 'kate', 'lubi', 'ani']
# print(guests)

# del guests[0]
# print(guests)

# sick_guest = guests.pop(0)
# print(guests)
# print(sick_guest.title())
# print(f"\n{sick_guest.title()} cannot attend to the dinner tonight, because unfortunately they have to isolate, regardless the rest will attend.")

# guests.append('mimi')
# guests.append('ira')
# guests.append('lora')
# print(guests)

# small_table = guests.pop()
# print(guests)

# Invite some people to dinner.
# guests = ['stella', 'kate', 'lubi']

# name = guests[0].title()
# print(f"{name}, please come to dinner.")

# name = guests[1].title()
# print(f"{name}, please come to dinner.")

# name = guests[2].title()
# print(f"{name}, please come to dinner.")

# name = guests[1].title()
# print(f"\nSorry, {name} can't make it to dinner.")

# # Kate cannot make it! Let's invite Ira instead.
# del(guests[1])
# guests.insert(1, 'Ira')

# # Print the invitations again.
# name = guests[0].title()
# print(f"\n{name}, please come to dinner.")

# name = guests[1].title()
# print(f"{name}, please come to dinner.")

# name = guests[2].title()
# print(f"{name}, please come to dinner.")

# # We got a bigger table, so let's add some more people to the list.
# print("\nWe got a bigger table!")
# guests.insert(0, 'Mimi')
# guests.insert(2, 'Laura')
# guests.append('Krisi')

# name = guests[0].title()
# print(f"{name}, please come to dinner.")

# name = guests[1].title()
# print(f"{name}, please come to dinner.")

# name = guests[2].title()
# print(f"{name}, please come to dinner.")

# name = guests[3].title()
# print(f"{name}, please come to dinner.")

# name = guests[4].title()
# print(f"{name}, please come to dinner.")

# name = guests[5].title()
# print(f"{name}, please come to dinner.")

# # Oh no, the table won't arrive on time!
# print("\nSorry, we can only invite two people to dinner.")

# name = guests.pop()
# print(f"Sorry, {name.title()} there's no room at the table.")

# name = guests.pop()
# print(f"Sorry, {name.title()} there's no room at the table.")

# name = guests.pop()
# print(f"Sorry, {name.title()} there's no room at the table.")

# name = guests.pop()
# print(f"Sorry, {name.title()} there's no room at the table.")

# # There should be two people left. Let's invite them.
# name = guests[0].title()
# print(f"{name}, please come to dinner.")

# name = guests[1].title()
# print(f"{name}, please come to dinner.")

# # Empty out the list.
# del(guests[0])
# del(guests[0])

# # Prove the list is empty.
# print(guests)
#  

# =======================================
# guests = ['lubi', 'kate', 'stella']
# name = guests[0].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")

# name = guests[1].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")

# name = guests[2].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")

# del(guests[1])
# guests.insert(1,'krisi')

# name = guests[0].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")

# name = guests[1].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")

# name = guests[2].title()
# print(f"\n{name}, you are invited to dinner at the Crocks!")


'''
Organsiing a list
'''

# cars = ['lada', 'bmw' ,'ferari', 'mercedes']
# cars.sort()
# print(cars)


# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#   print(magician)   
  
  
# favourite_pizzas = ['margarita', 'quatro fromage', 'vegetariana']
# for pizza in favourite_pizzas:
#   print(pizza)
#   print(f"I love {pizza.title()}!")

# ===== the difference in the code only because one is indented and the other one not 

# favourite_pizzas = ['margarita', 'quatro fromage', 'vegetariana']
# for pizza in favourite_pizzas:
#   print(pizza)
# print(f"I love {pizza.title()}!")

'''
Making  Numerical list
'''

# ===== Using range () Function  

# for value in range(1, 5):
#   print(value)

# for value in range(1,6):
#  print(value)

# for value in range(7):
#   print(value)

'''
Using range() to make a list of numbers
'''

# numbers = list(range(1,6))
# print(numbers)

# numbers = tuple(range(1, 6))
# print(numbers)

# even_numbers = list(range(2,13,2))
# print(even_numbers)

# ===> the space between the values in that case does not matter

# even_numbers = list(range(2,13,2))
# print(even_numbers)


# any_numbers = list(range(2, 12, 1))
# print(any_numbers)

# squares = []
# for value in range (1, 11):
#   square = value ** 2
#   squares.append(square)

# print(squares)

# # === or another way of writing that code more concisely

# squares = []
# for value in range(1,11):
#   squares.append(value ** 2)

# print(squares)  

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# digits = [174657486, 2389579498766878837, 30293098, 4465794, 4985765985, 30848566, 75654787, 3907540008, 2090399, 98]
# print(min(digits))
# print(max(digits))
# print(sum(digits))


'''
LIST COMPREHENSIONS
'''

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# == try it yourself

# for value in range(1, 21):
#   print(value)

# for value in range(1, 1000000):
#   print(value)

# numbers = list(range(1, 1000000))
# print(numbers)

# numbers = list(range(1, 100))
# print(numbers)

# numbers = list(range(1, 1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))


# for value in range(1, 21, 4):
#   print(value)

# threes = list(range(3, 31, 3))
# for number in threes:
#   print(number)

# cubes = []
# for values in range(1, 11):
#   cubes.append(values**3)

# print(cubes)  

# cubes = [values**3 for values in range(1, 11)]
# print(cubes)


# players = ['charles', 'martina', 'bonnie', 'florence', 'kewin']
# print(players[0:3])

players = ['charles', 'martina', 'bonnie', 'florence', 'kewin']
# print(players[1:4])
# print(players[:4])
# print(players[4:])

# print(players[-3:])
# print(players[1:3])

'''
Copying a list
'''

# my_food = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_food[:]
# print(friend_food)

# print("My favourite foods are:")
# print(my_food)

# print("\nMy friend's favourite foods are:")
# print(friend_food)



# ===========

# restaurant_menu = ('chips', 'pizza slice', 'salad', 'falafels wrap')
# print("This menu includes all the meals that restaurant offers")
# for food in restaurant_menu:
#   print(food.title())

# print(restaurant_menu[2].title())

# # restaurant_menu[2] = "banana bread"
# # print(restaurant_menu)

# restaurant_menu = ('chips', 'pizza slice', 'guliash', 'vegan masala')
# print("This is our reniewed menu from July 2021")
# for food in restaurant_menu:
#   print(food)


# =========
'''
lists slicing
'''

# players = ['buddy', 'gosho', 'mitro', 'abbie', 'elza']
# print(players[2:])
# print(players[-3:])

# print(players[1:3])
# print(players[-4:-2])
# for player in players[2:]:
#     print(player.title())

'''
copying a list
'''

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favourite foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friend_foods)

# ======== different example

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favourite foods are:")
# print(my_foods)

# print("\nMy friend's favourite foods are:")
# print(friend_foods)


# ==== try it yourself

# my_list = ['cat', 'dog', 'mouse', 'parrot']
# print("The first three items in the list are:")
# # print(my_list[0:3])
# for items in my_list[0:3]:
#     print("-" + items.title())


# print("Three items from the middle of the list are:")
# for items in my_list[1:3]:
#     print("-" + items.title())

# print("The last three items in my list are:")
# for items in my_list[1:]:
#     print("-"+items.title())

'''
TUPLES
'''

# ==== TUPLES are immutable lists. Creating a list thta cannot change

# ====> We cannot modify a tuple, but we can assign new value to a variable that represents a tuple. So if we want to cgange our dimensions, we could redefine the entire tuple:

# dimensions = (200, 5)
# print(dimensions[0])
# print(dimensions[1])

# => we define a tuple by parentheses instead of using square brackets. We print each element in a tuple by using the same syntax we have been using to access an element in a list.

# dimensions = (200, 5)
# dimensions[0] = 250
# print(dimensions)

# == This shows that we cannot changes values in a tuple
 

#  ======= Looping though a Tuple

# dimensions = (200, 5)
# for dimension in dimensions:
#     print(dimension)

#  ======= Writing over a Tuple

# dimensions = (200, 5)
# print("Original dimensions are:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions are:")
# for dimension in dimensions:
#     print(dimension)