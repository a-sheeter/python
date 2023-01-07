#You know the drill.

#1. Sum Values: This function should sum up all of the values from the key-value pairs in the dictionary.

def sum_values(my_dictionary):
  total = 0;
  for values in my_dictionary.values():
    total += values
  return total

#test function
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#2. Even Keys: Loop through a dictionary and return the values ONLY if the key is even.

def sum_even_keys(my_dictionary):
  total = 0;
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary.get(key)
  return total

#test function
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#3. Add Ten: Loop through a dictionary and add 10 to the value. Return the dictionary with the updated values.

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] = my_dictionary.get(key) + 10
  return my_dictionary

#test function
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

