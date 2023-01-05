#This is a program that creates menu, franchise and business classes

from datetime import time

#creating menus
#menu types: brunch, early-bird, dinner, kids
class Menu:
  #constructors: basically, attributes that are just declared automatically
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #repr: allows you to access the constructors
  def __repr__(self):
    return self.name, self.items, self.start_time, self.end_time

  #str allows you to print 
  def __str__(self):
    return "This is the {} menu that is available from {} to {}.".format(self.name, str(self.start_time), str(self.end_time))

  #calculate bill method
  def calculate_bill(self, purchased_items):
    items = self.items
    keys = items.keys()
    total_bill = 0;

    for item in purchased_items:
      for key in keys:
        if item == key:
          total_bill += items.get(key)
    return f'${total_bill:.2f}'
    
#declarations new objects using class Menu
brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11), time(16))

early_bird = Menu('early-bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, time(15), time(18))

dinner = Menu('dinner', {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'ducl ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, time(17), time(21))

kids = Menu('kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11), time(21))

arepas = Menu('arepas', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, time(10), time(20))

#creating franchises
class Franchise:
  def __init__(self, name, address, menus):
    self.name = name
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.name, self.address
  
  def __str__(self):
    return "This is the {} location, and you can find it at {}.".format(self.name, self.address)

  def return_menus(self):
    list_of_menus = []
    for menu in self.menus:
      list_of_menus.append(menu.name)
    return list_of_menus

  def available_menus(self, time):
    #list for menus available and not available
    are_available = []
    not_available = []
    for menu in self.menus:
      #need to turn the dates into int to compare 
      start_time = int(menu.start_time.strftime("%H"))
      end_time = int(menu.end_time.strftime("%H"))
      input_time = int(time.strftime("%H"))
      #comparing start and end times with input time
      if input_time >= start_time and input_time <= end_time:
        are_available.append(menu.name)
      else:
        not_available.append(menu.name)
    return are_available

#instances of franchises
flagship_store = Franchise("Flagship Store", "1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("New Installment", "12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchise("Arepas", "189 Fitzgerald Avenue", [arepas])

#creating businesses 
class Business:
  #constructors
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
  def __repr__(self):
    return self.name, self.franchises

#business instantiation
arepas_business = Business("Take a' Arepa", arepas_place)


