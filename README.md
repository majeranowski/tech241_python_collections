# Collections in Python

### Lists 

List is an array. It is a collection of data types

Creating a list:

```python
shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
```

accessing certain parts of list:
We can use indexing:

```python
print(shopping_list[0])
```

change a specific element of my list:

```python
shopping_list[4] = "orange juice"
```

### List methods

* .append()

add something to the list at the end of the list

* .remove()

remove the element from the list

* .pop()

remove the last element from the list (if you add index it will remove the specific index from the list)

### List can be a collection of different data types

##### List slicing

```python
mixture = [1, 2, 3, "one", "two", True]
print(mixture)
print(mixture[1:3]) # 2, 3

print(mixture[::2]) #1, 3, 'two' when you put :: it means every second step skip over
```

### Tuples

 () - Tuples are immutable, so they cannot be changed.
 
```python
essentials = ("bread", "eggs", "milk")
print(essentials)
# counting how many times appeared in the tuple
print(essentials.count("bread"))
```
### Dictionaries

Key - value pairs / Key is the name/reference, Value is the data stored

```python
student_1 = {
    "name": "Krzysztof",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_name": ["variables", "git", "data_types", "collections"]
}
```

How to access parts of a dictionary

```python
print(student_1["stream"]) #devops
print(student_1["completed_lesson_name"][0]) #variables
```

Changing a value

```python
student_1["completed_lessons"] = 3

student_1["completed_lesson_name"].remove("data_types")

print(student_1["completed_lesson_name"])
```

Dictionaries methods:

* .keys() - gives the keys of the dict

`print(student_1.keys())`

* .values() - gives the values of keys in dict

`print(student_1.values())`

### Sets

{} - Sets are the lists but unordered
```python
car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts)
```


add to a set
```python
car_parts.add("doors")
print(car_parts)
```


remove from a set
```python
car_parts.remove("doors")
print(car_parts)
```


### frozen set
frozen set is like a set but immutable
```python
x = frozenset(["eggs", "bread", "butter"])
print(x)
```
