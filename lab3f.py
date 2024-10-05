#!/usr/bin/env python3
# Author ID- isingh176

# Initialize the list
my_list = [1, 2, 3, 4, 5]

# Function to add a new item to the list
def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_value = ordered_list[-1] + 1
    ordered_list.append(new_value)

# Function to remove specific items from the list
def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values in items_to_remove from the ordered_list
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    # Initial list output
    print(my_list)
    
    # Adding items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    
    # Removing items [1, 5, 6] from the list
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)
