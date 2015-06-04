#for use of the shopping list script

shopping_list = list()

def show_help():
'''Show commands needed for shopping list'''
    print("What should we pick up at the store?")
    print("Enter DONE to stop adding items. Enter HELP for this help. Enter SHOW if you want to see what you added so far. ")

def add_to_list(new_item):
'''Add new items to shopping list'''
    shopping_list.append(new_item)
    print("Added to list: {} ".format(new_item))
    print("List now has {} items ".format(len(shopping_list)))

def show_list(shopping_list):
'''Show the list written done so far'''
    print("Here is your list: ")
    for s in shopping_list:
        print(s)
    

show_help()
while True:
    new_item = input("Item? ")
    if new_item == "DONE":
        show_list(shopping_list)
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list(shopping_list)
        continue 
    add_to_list(new_item)
    continue 

#show_list(shopping_list)

