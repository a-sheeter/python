# Python code challenges; Tests critical thinking skills to write programs that accomplish separate tasks; Each mini test will be separated by comments explaining the challenge

# Python Challenges: STRINGS
# 1. Count Letters - Count the number of unique letters in a string. This means that when we are looking at the word, any new letters should be counted and any duplicates should not be counted. There are a few ways to solve this, but we can use the provided alphabet string to ensure that duplicates are not counted. 

def unique_english_letters(string):
  counter = 0;
  letters_used = []

  for letter in string:
    letters_used.append(letter)
    if letters_used.count(letter) == 1:
      counter += 1
  return counter

#test the function
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# 2. Count X - Count the number of occurrences of a certain letter within a string. Our function will accept a parameter for a string and another for the character which we are going to count.

def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

#test function
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# 3. Count Multi X: This function should accept a string and a substring to compare against. The number of occurrences of the second parameter within the first parameter string are returned. What this means is that we are checking the number of occurrences of the shorter string (second parameter) within the longer string (first parameter). 

def count_multi_char_x(word, x):
  split_string = word.split(x)
  return len(split_string) - 1

# test function
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# 4. Substring Between: Create a function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the ending character of our substring. 

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)

  if start_index != -1 and end_index != -1:
    return word[start_index+1:end_index]
  else:
    return word

#test function
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5. X Length: We need a new function that is able to accept two inputs: one for a sentence and another for a number. The function returns True if every single word in the sentence has a length greater than or equal to the number provided.

def x_length_words(sentence, num):
  sent_array = sentence.split(" ")
  for word in sent_array:
    if len(word) < num:
      return False
    else:
      return True

#test function
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#New set: More Advanced

#1. Check Name: Create a function that is able to check if a user’s name is located within their greeting. We need a function that accepts two parameters, a string for our sentence and a string for a name. The function should return True if the name exists within the string (ignoring any differences in capitalization).

def check_for_name(sentence, name):
  sent_array = sentence.split(" ")
  is_name_found = True;
  for word in sent_array:
    if word.lower() == name.lower():
      is_name_found = True
    else: 
      is_name_found = False
  return is_name_found

#test function
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#easier solution: def check_for_name(sentence, name): return name.lower() in sentence.lower()

#2. Every Other Letter: create a function that extract every other letter from a string and returns the resulting string. 

def every_other_letter(word):
  new_string = ""
  for i in range(len(word)):
    if i%2==0:
      new_string += word[i]
  return new_string

#test function
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd

#3. Reverse: we want to reverse the entire string. 

def reverse_string(word):
  reversed_string = ""
  for i in range(1, len(word)+1):
    reversed_string += word[-i]
  return reversed_string

#test function
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH

#4. Make Spoonerism: switch the first letter of the first and second words

def make_spoonerism(word1, word2):
  return word2[0] + word1[1:] + " " + word1[0] + word2[1:]
 
#test function
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#5. Add exclamation: Our function will accept a string and if the size is less than 20, it will fill in the remaining space with exclamation marks until the size reaches 20. If the provided string already has a length greater than 20, then we will simply return the original string. 

def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  return word

#test function
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn












