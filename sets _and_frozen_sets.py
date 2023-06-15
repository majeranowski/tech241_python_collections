# Sets and Frozen Sets

# {} - Sets are the lists but unordered

car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts)

# add to a set

car_parts.add("doors")
print(car_parts)

# remove from a set

car_parts.remove("doors")
print(car_parts)

# frozen set is like a set but immutable

x = frozenset(["eggs", "bread", "butter"])
print(x)