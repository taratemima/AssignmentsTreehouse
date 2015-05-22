import random

name = "Tara"
treehouse ="Tree"+"house" 
email_greeting = "{} loves {}".format(treehouse, name)

age = 38
days = int(age) * 52 * 7
summary = "I am  {} days old!".format(days)

def add_list(listOfNum):
  total = 0
  for n in listOfNum:
    total += n
  return total 

def summarize(listOfNum):
  total = add_list(listOfNum)
  return "The sum of {} is {}.".format(listOfNum, total)

def random_num(number):
  return random.randint(1, number) 

list_1 = ["pear","peach","plum"]
list_2 = ["apple","pumpkin","cherry"]
list_3 = list_1+list_2

the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
the_list.insert(0, the_list.pop(3))
the_list.remove("a")
the_list.remove(False)
the_list.remove([1,2,3])
the_list.extend([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

messy_list = [5, 2, 1, 3, 4, 7, 8, 0, 9, -1]

# Your code goes below here
clean_list = messy_list[:]
clean_list.sort()

def first_4(sampleList):
  return sampleList[:4]

def odds(sampleList):
  return sampleList[1::2] 

def first_and_last_4(sampleList):
  first4 = sampleList[:4]
  last4 = sampleList[-4:]
  return first4+last4

def sillycase(sampleString):
  midpoint = round(int(len(sampleString))/2)
  firstPart = sampleString[:midpoint].lower()
  lastPart = sampleString[midpoint:].upper()
  return firstPart+lastPart

def members(used_dict, keylist):
  total = 0
  for k in keylist:
    if k in used_dict.keys():
      total += 1
  return total

def word_count(sampleString):
  newDict = dict()
  wordlist = sampleString.split()
  for w in wordlist:
    if w in newDict.keys():
      newDict[w] += 1
    else:
      newDict[w] = 1
  return newDict

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"
statements = list()
def string_factory(dicts, string):
  for d in dicts:
    statements.append(string.format(**d))
  return statements

def most_classes(teacherDict):
  max_count = 0
  answer = ''
  for teacher, classList in teacherDict.items():
    if len(classList) > max_count:
      max_count = len(classList)
      answer = teacher
  return answer 

def num_teachers(teacherDict):
  return len(teacherDict.keys())

def stats(teacherDict):
  listOflists = list()
  for teacher, classList in teacherDict.items():
    listOflists.append([teacher, len(classList)])
  return listOflists 

def courses(teacherDict):
  all_classes = list()
  for v in teacherDict.values():
    all_classes.extend(v)
  return all_classes

#I first did courses with two for loops.  I decided to take a list convulted route for lists

def stringcases(sampleString):
  return (sampleString.upper(), sampleString.lower(), sampleString.title(), sampleString[::-1])

#last one reverses the string, and does str have reverse as a method?

def combo(iter1, iter2):
  tupleList = list()
  for index1, item1 in enumerate(iter1):
    for index2, item2 in enumerate(iter2):
      if index1 == index2:
        tupleList.append((item1, item2))
  return tupleList 
