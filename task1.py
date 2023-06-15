'''
Define a list with some cool things inside. E.g. things you would buy if you were a millionaire. The list must have at least 5 elements.

First, print the list and check it's type

Print the list's first element

Print the list's second element

Print the list's last element using negative indexing

Replace the first item in the list

Replace another item in the list and print the list

Add a new item to the list, print the list

Remove an item from the list, print the list

Remove the last item from the list without specifying what it is (hint, there is a list method to do this)
'''

things = ["yacht", "house", "car", "watch", "another car"]

# Print the list and check its type
print(things)
print(type(things))

# Print 1st element
print(things[0])

# Print 2nd element
print(things[1])

# Print the last element using negative indexing
print(things[-1])

# Replace the first item in the list
things[0] = "loft"
print(things)

# Replace another item in the list and print the list
things[2] = "Island"
print(things)

# Add a new item to the list
things.append("sushi omasake meal")
print(things)

# Remove an item from the list
things.remove("house")
print(things)

# Remove the last item from the list
things.pop()
print(things)