# Define the to-do list
todo_list = []

# Define a function to add an item to the list
def add_item(item):
    todo_list.append(item)
    print(f"{item} added to the list")

# Define a function to remove an item from the list
def remove_item(item):
    todo_list.remove(item)
    print(f"{item} removed from the list")

# Define a function to view the items in the list
def view_list():
    for item in todo_list:
        print(item)

# Add some items to the list
add_item("Take out the trash")
add_item("Buy groceries")
add_item("Do laundry")

# View the list
view_list()

# Remove an item from the list
remove_item("Do laundry")

# View the list again
view_list()
