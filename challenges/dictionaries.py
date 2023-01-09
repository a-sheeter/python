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

#4. Values in Keys: Check if values in a dictionary are also keys
def values_that_are_keys(my_dictionary):
  list_values = []
  values_also_keys = []
  for value in my_dictionary.values():
    list_values.append(value)
  for key in my_dictionary.keys():
    for i in range(len(list_values)):
      if key == list_values[i]:
        values_also_keys.append(list_values[i])
  return values_also_keys


#test functions
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#5. Largest Value: return the key with the largest value

def max_key(my_dictionary):
  max_value = float("-inf");
  max_key = float("-inf");
  for key, value in my_dictionary.items():
    if value > max_value:
      max_value = value
      max_key = key
  return max_key

#test function
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

#More Advanced Challenges

#1. Word length Dict: create a dictionary that takes in a list of strings and makes the key the string and the value the length of the string

def word_length_dictionary(words):
  my_dictionary = {}
  for word in words:
    my_dictionary.update({word:len(word)})
  return my_dictionary


#test function
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#2. Frequency Count: return a dictionary that takes in a list of strings and returns their frequency in the string as the value.
def frequency_dictionary(words):
  my_dictionary = {}
  for word in words:
    if word not in my_dictionary:
      my_dictionary[word] = 0
      my_dictionary[word] += 1
    else:
      my_dictionary[word] += 1
  return my_dictionary


#test function
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#3. Unique Values: take a dictionary as input and return the number of unique values
def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)

#test function
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1



