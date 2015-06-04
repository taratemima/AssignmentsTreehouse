shopping_list = list()

def show_help():
'''Show menu and instructions'''
    print("\nSeparate each item with a comma. ")
    print("Enter DONE when you are finished adding to the list, SHOW to see the current items in the list, and HELP for this message. ")

def show_list():
'''Show list created so far'''
    count = 1
    for new_item in shopping_list:
        print("{}:{}".format(count, new_item))
        count += 1
        #I realize this is not how most Python developers handle this problem. I kept it in to show what I knew at the time of the course


print("Give me a list of things that you want to buy at the grocery store: ")
show_help()

while True:
    new_stuff = input("Your list? ")

    if new_stuff == "DONE":
        print("\nHere is your list: ")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    else:
        new_list = new_stuff.split(',')
        #for n in new_list:
         #   print(n)
         #OK, I thought it was putting spaces in the list
         #However, when I did that, I still got the right amount, wrong item problem
        index = input("Add this in a certain spot? Press ENTER for the end of the list."
                      "Or give me a number for the placeholder on the list."
                      "Currently we have {} items in our list. ").format(len(shopping_list))
        if index:
            try:
                spot = int(index) - 1
            except:
                print("That number is not in our list. ")
                continue 
             
             #Using the try/except statement just had the last item added three times.
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
            
#Make it possible to move items from one position to another
#Change the formatting of the list display
#Create a CLEAR command that removes everything from the list
          
