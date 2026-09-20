#******************************************************************************
# vickrey.py
#******************************************************************************
# Name: 
#******************************************************************************
# Overall remarks (not to replace in-line comments):
#
#
#
#


# HERE ARE PROMPT AND OTHER MESSAGES TO USE
# SO THAT THE AUTOGRADER RECOGNIZES YOUR SOLUTION AS CORRECT'Enter Latitude of Car 1: '

bid1 = float(input('Bid 1: '))
bid2 = float(input('Bid 2: '))
bid3 = float(input('Bid 3: '))
bid4 = float(input('Bid 4: '))

if bid1 > bid2 and bid1 > bid3 and bid1 > bid4:
    print('Winner is:')
    print('Bid 1')
    print('Price paid:')
    if bid2 > bid3 and bid2 > bid4:
        print(bid2)
    elif bid3 > bid2 and bid3 > bid4:
        print(bid3)
    else:
        print(bid4)
elif bid2 > bid1 and bid2 > bid3 and bid2 > bid4:
    print('Winner is:')
    print('Bid 2')
    print('Price paid:')
    if bid1 > bid3 and bid1 > bid4:
        print(bid1)
    elif bid3 > bid1 and bid3 > bid4:
        print(bid3)
    else:
        print(bid4)
elif bid3 > bid1 and bid3 > bid2 and bid3 > bid4:
    print('Winner is:')
    print('Bid 3')
    print('Price paid:')
    if bid1 > bid2 and bid1 > bid4:
        print(bid1)
    elif bid2 > bid1 and bid2 > bid4:
        print(bid2)
    else:
        print(bid4)
else:
    print('Winner is:')
    print('Bid 4')
    print('Price paid:')
    if bid1 > bid2 and bid1 > bid3:
        print(bid1)
    elif bid2 > bid1 and bid2 > bid3:
        print(bid2)
    else:
        print(bid3)
