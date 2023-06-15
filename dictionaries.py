# Dictionaries

# Key - value pairs / Key is the name/reference, Value is the data stored

# Making a dictionary

student_1 = {
    "name": "Krzysztof",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lesson_name": ["variables", "git", "data_types", "collections"]
}

print(student_1)

# How to access parts of a dictionary
print(student_1["stream"])
print(student_1["completed_lesson_name"][0])

# changing a value

student_1["completed_lessons"] = 3

student_1["completed_lesson_name"].remove("data_types")

print(student_1["completed_lesson_name"])

# Dictionary methods
#gives the keys of the dict
print(student_1.keys())

#gives the values of keys in dict
print(student_1.values())