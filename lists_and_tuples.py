# Lists and Tuples

# List is an array

# making a list in Python

shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]

print(type(shopping_list))
print(shopping_list)

#accessing certain parts of list
#indexing

print(shopping_list[0])

# change a specific element of my list

shopping_list[4] = "orange juice"
print(shopping_list)

# list methods

# add something to the list at the end of the list

shopping_list.append("butter")
print(shopping_list)

# remove the element from the list
#
shopping_list.remove("butter")
print(shopping_list)

# remove the last element from the list (if you add index it will remove the specific index from the list)

shopping_list.pop()
print(shopping_list)

#list can be a mixed of different data types
# list slicing
mixture = [1, 2, 3, "one", "two", True]
print(mixture)
print(mixture[1:3]) # 2, 3

print(mixture[::2]) #1, 3, 'two' when you put :: it means every second step skip over

# Tuples

# () - Tuples are immutable, so they cannot be changed.

essentials = ("bread", "eggs", "milk")
print(essentials)
# counting how many times appeared in the tuple
print(essentials.count("bread"))