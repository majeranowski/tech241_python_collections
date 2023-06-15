'''
Your Hero Story!

This is all about dictionaries. Note the method I didn’t show in class was .items(). it returns the key values pairs in the dictionary back as a list of tuples. Try it out!

Summary
Your going to write a story, cut it into section, store the section in a python dictionary!

Tasks

define a dictionary

add your content as values for keys

follow the instruction in the pseudo code below:

**Dictionary basics :D
**
1 - Define a dictionary call story1, it should have the following keys:
#"start", "middle" and "end"

2 - Print the entire dictionary

3 - Print the type of your dictionary

4 - Print only the keys

5 - Print only the values

6 - Print the individual values using the keys (individually, lots of print commands)

7 - Now let's add a new key:value pair.
# "hero": "yourSuperHero"

Acceptance Criteria:

All 7 tasks are done
Runs with no errors
'''

story1 = {
    "start": "Once upon a time, in a galaxy not that far away, in the greatest country in the World - United Kingdom...",
    "middle": "The guy tired of his life because he was already after 30 started a journey for a brighter future. Frustrated with previous missions and figting enemies in a land called Retail,\n"
              "he jumped in his ship and sailed to an ancient Greece - Sparta. He had to leave his friendly horse named Mac behind as in Sparta there was no place for such horses as Mac. \n"
              "Completely alone in a new land he set up the base and waited for new things to come.\n"
              "Right after that he was attacked by a giant snake named Python. Python had 3 heads that's why local people in Sparta called him Python3.\n"
              "Our gur knew he could not beat him on his own. He needed help and help arrived. It was a Mac? No, this horse just looked like Mac. It was black horse called Windows...",
    "end": "Together with Windows our guy beat the Python to death. What will happen next? Who knows but local people say something about another creature terrorizing the Sparta called Azure.",
}

# Print the entire dictionary
print(story1)

# Print the type of the dictionary
print(type(story1))

# Print only the keys
print(story1.keys())

# Print only the values
print(story1.values())

# Print the individual values using the keys
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Add a new key-value pair to the dictionary
story1["hero"] = "Super Polishman"

# Print the updated dictionary
print(story1)