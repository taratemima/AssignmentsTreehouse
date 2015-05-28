import re

file_object = open("basics.txt") 
data = file_object.read()
file_object.close()
first = re.match(r'Four', data) 
liberty = re.search(r'Liberty', data)

def first_number(data_string):
  return re.search(r'\d', data_string)

def numbers(count_int, count_string):
  return re.search(r'\d' * count_int, count_string)

