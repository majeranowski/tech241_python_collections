'''
You are going to make a program that helps a waiter with their menu

3- 5 starters
3-5 mains
3-5 desserts

Make a new file called ‘waiter_helper.py’

See the user stories and complete the task accordingly using lists:

User stories:

As a user, I want to be able to see the menu in a formatted way so that I can order my meal.

As a user, I want to be able to order three separate times and have my responses added to a list so they are not forgotten.

As a user, I want to have my order read back to me in a formatted way so I know what I ordered.
'''
# creating a menu list
menu = ['burata', 'tartare', 'salad','salmon', 'chicken', 'duck', 'strudel', 'cheesecake', 'cherry pie']
# creating an empty list for client order

client_order = []
#variable controlling a loop
loop = True
# while loop to ask for a user input
while loop:
    print("What would you like to do ? \n"
      "1. See the menu\n"
      "2. Order\n"
      "3. See my order\n"
      "4. Finish")
    choice = int(input("choose: "))
# if statements for different inputs
    if choice == 1:
        print(menu)
    elif choice == 2:
        order = input("Enter your order: ")
        client_order.append(order)
    elif choice == 3:
     print(client_order)
    else:
        loop = False
