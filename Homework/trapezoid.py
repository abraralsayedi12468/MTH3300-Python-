#******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#NONE 
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

#DEFINE YOUR FUNCTION f HERE:
    
def f(x):
    import math 
    k = math.sqrt(1 + (math.sin(x)**2))
    return k
    


#CODE FOR GETTING THE INPUT:

x = 0
a = float(input('Enter the lower bound: '))
b = float(input('Enter the upper bound: '))
n = int(input('Enter the number of trapezoids: '))

deltaX = (b-a)/n
aprox = 0

for i in range(n+1):
    x = a + i*deltaX
    
    if i == 0 or i == n:
        aprox += f(x)
    else:
        aprox += 2*f(x)

aprox = (deltaX/2)*aprox
            



################################################

#CODE FOR PRINTING THE APPROXIMATION TO 8 DECIMAL PLACES
print(f'The definite integral is approximately: {aprox:.8f}')