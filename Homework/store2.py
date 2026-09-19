#******************************************************************************
# store2.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#Your Office hours and our class lectures :) 
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#This may be concerning, but this took me WAYYY too long to figure out.
#
# 
# 

# Here are you pre-defined items and corresponding prices. 
# Do not modify these lists

items = ["Apple", "Banana", "Orange", "Grapes", "Watermelon",
         "Chicken Breast", "Ground Beef", "Salmon", "Bacon", "Eggs",
         "Milk", "Cheese", "Yogurt", "Butter", "Bread",
         "Rice", "Pasta", "Cereal", "Chocolate", "Chips"]

prices = [1.20, 0.50, 0.80, 2.50, 3.00,
          5.50, 6.80, 9.20, 4.30, 2.50,
          3.20, 4.50, 1.80, 3.60, 2.40,
          1.90, 1.70, 4.10, 2.50, 3.20]

###### Your code starts here! ############
tax = 0.08
total = 0
index = ''
not_found = ''

item = input('Enter item name or PAY to end your order. ')

while item != 'PAY': 
    count = int(input(f'How many {item}s are you buying? '))
    try:
        index = items.index(item)
        price = prices[index]
        total += price * count

    except ValueError:
        not_found += f'Item {item} not found and ignored.'

    item = input('What are you buying? Enter PAY to end your order. ')

print('We will now calculate your total order!')
if not_found != '': 
    print(not_found)

total_with_tax = total + (total * tax)

print(f'Your total before tax is ${total:.2f}')
print(f'Your total is ${total_with_tax:.2f}')
