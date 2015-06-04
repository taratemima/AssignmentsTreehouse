'''Simple version of shopping list'''

shopping_list = list()

print("What should we pick up at the store?")
print("Enter DONE to stop adding items")

while True:
    new_item = input("Item? ")
    if new_item == "DONE":
        break
    shopping_list.append(new_item)
    print("Added to list: {} ".format(new_item))
    print("List now has {} items ".format(len(shopping_list)))
    continue

print("Here is your list: ")

for s in shopping_list:
    print(s)
    
