#******************************************************************************
# store3.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://chatgpt.com/share/6a7aa865-34d0-83ea-8b9b-87a5112cbc02
# I mainly used ai to replace the items varibles using the class using self._items and assigning to self._invetory 
#because it wouldve gotten tedious and confusing had i went in and chnaged each thing myself :) 
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 


class Store:
    def __init__(self, name):
        self._name = name
        self._inventory = {}

    def update_inventory(self, item):
        self._inventory[item._name] = item
        
#testing :) 
#bigstore = Store(’BigSavings’)
#print(bigstore._name)
#print(bigstore._inventory)

    def POS(self):
        tax = 0.08
        total = 0
        not_found = ''
    
        item = input('Enter item name or PAY to end your order. ')
    
        while item != 'PAY':
            count = int(input(f'How many {item}s are you buying? '))
    
            try:
                current_item = self._inventory[item]
                price = current_item._sales_price
                total += price * count
                current_item._inv -= count
    
            except KeyError:
                not_found += f'Item {item} not found and ignored.\n'
    
            item = input(
                'What are you buying? Enter PAY to end your order. ' )
    
        print('We will now calculate your total order!')
    
        if not_found != '':
            print(not_found)
    
        total_with_tax = total + (total * tax)
    
        print(f'Your total before tax is ${total:.2f}')
        print(f'Your total is ${total_with_tax:.2f}')
    

    def sale(self, sale):
        for i in self._inventory:
            current_item = self._inventory[i]
            current_item._sales_price -= current_item._sales_price * (sale / 100)
        return self._inventory     
    

class Item:
    def __init__(self, n, c, sp, i):
        self._name = n
        self._cost = c
        self._sales_price = sp
        self._inv = i
        
    def _add_inv(self, quantity):
        self._inv += quantity 
    
    def _change_cost(self, new_cost):
        self._cost = new_cost
        
    def _change_sales_price(self, new_sales_price):
        self._sales_price = new_sales_price

#test run 
#bigstore = Store('BigSavings')

#print(bigstore._name)
#print(bigstore._inventory)

#apple = Item('Apple', 0.60, 1.20, 10)

#print(apple._name)
#print(apple._cost)
#print(apple._sales_price)
#print(apple._inv)


#bigstore.update_inventory(apple)

#print(bigstore._inventory['Apple']._name)
#print(bigstore._inventory['Apple']._sales_price)
#print(bigstore._inventory['Apple']._inv)

















