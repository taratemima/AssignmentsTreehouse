
import datetime 
from collections import OrderedDict
import sys
import os

from peewee import *

#Needs to be checked

#!/usr/bin/env/python3

db = SqliteDatabase('diary.db')

class Entry(Model):
'''Set up instance of Entry from Model'''
    # content
    content = TextField()
    # timestamp
    timestamp = DateTimeField(default=datetime.datetime.now) 
    
    class Meta:
        database = db
        

def menu_loop():
    """Show the menu"""
    choice = None
    while(choice != 'q'):
      clear()
      print("Enter 'q' to quit")
      for key, value in menu.items():
        print("{}) {}".format(key, value, __doc__))
        choice = input("Action: ").lower().strip()
        if choice in menu:
          clear()
          menu[choice]()
          

def initialize():
  '''Create diary if it does not exist'''
  db.connect()
  db.create_tables([Entry], safe=True)
  

def clear():
'''Clear screen from system calls'''
    os.system('cls' if os.name == 'nt' else 'clear')    

def add_entry():
    """Add an entry."""
    print("Add your entry. Press control+d when finished")
    data = sys.stdin.read().strip()
    if data:
        if(input("Save entry? Y/n ").lower() != 'n'):
            Entry.create(content=data)
            print("Saved successfully")

def view_entries(search_query = None):
    """View previous entries."""
    if(search_query):
        entries = entries.where(Entry.content.contains(search_query))


    entries = Entry.select().order_by(Entry.timestamp.desc())
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp)) 
        print('n: next entry ')
        print('d: delete entry ')
        print('q: return to menu ')
        next_action = input('Action: Ndq').lower().strip() 
        if(next_action == 'q'):
            break
        elif(next_action == 'd'):
            delete_entry(entry)


def search_entries():
    """Search entries for a string"""
    view_entries(input("Search query: "))

    
def delete_entry(entry):
    """Delete an entry."""
    if(input("Are you sure that you want to delete the entry? [yN] ").lower() == 'y'):
        entry.delete_instance()
        print("Entry deleted. ")


    
menu = OrderedDict([
  ('a', add_entry),
  ('v', view_entries),
  ('s', search_entries)
  ])

if __name__ == '__main__':
    initialize() 
    menu_loop()
    

#Use textwrap and Blessings to make your application more professional and interesting.