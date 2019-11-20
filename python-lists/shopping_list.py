# Create a new empty list named shopping_list
shopping_list = []

def show_help():
    print("What should we pcik up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to view the full list.
""")

    
# Create a function called add_to_list that declares a parameter named item
def add_to_list(item):
    # Add the item to the list
    shopping_list.append(item)
    # Notify user that the item was added, and state the number of items in the list currently
    print("Added! List has {} items.".format(len(shopping_list)))

    
# Define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print("* {}".format(item))
    
show_help()
    
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    # Enable the SHOW command to show the list. Don't forget to update the HELP documentation
    elif new_item == "SHOW":
        show_list()
        continue
        
    # Call add_to_list with new_item as the argument
    add_to_list(new_item)
    
show_list()