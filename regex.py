import re

file_object = open("basics.txt") 
data = file_object.read()
file_object.close()
first = re.match(r'Four', data) 
liberty = re.search(r'Liberty', data)

def first_number(data_string):
'''Find the first number in a string'''
  return re.search(r'\d', data_string)

def numbers(count_int, count_string):
'''Find all numbers in a string'''
  return re.search(r'\d' * count_int, count_string)

#contacts = re.search(r'(?P<email>[-\w\d.+]+@[-\w\d.]+),\s(?P<phone>\d{3}-\d{3}-\d{4})', string, re.X|re.M)
#twitters = re.search(r'@\w+$', string, re.MULTILINE)


string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search("""
    (?P<last_name>\w+?\s*\w*)(?:,\s)
    (?P<first_name>\w+?\s*\w*)(?:\:\s)
    (?P<score>\d+)
""", string, re.I|re.M|re.X)

class Player:
'''Create class for player name and scores'''
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score

#needs to be tested in the complier

