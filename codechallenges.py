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
