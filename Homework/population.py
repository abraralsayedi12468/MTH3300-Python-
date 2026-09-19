#******************************************************************************
# population.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Overall remarks (not to replace in-line comments):
#
#
#
#


# HERE ARE THE PROMPT MESSAGES TO USE SO THAT THE AUTOGRADER 
# RECOGNIZES YOUR SOLUTION AS CORRECT

import math 
P = float(input('Enter initial population: '))
t1 = float(input('Enter first time period (in years): '))
r1 = float(input('Enter first growth rate (in percent): '))
P= P * math.exp((r1/100) * t1)
t2 = float(input('Enter second time period (in years): '))
r2 = float(input('Enter second growth rate (in percent): '))
P= P * math.exp((r2 / 100) * t2)
t3 = float(input('Enter third time period (in years): '))
r3 = float(input('Enter third growth rate (in percent): '))
P= P * math.exp((r3 / 100) * t3)


print(f'The final population is:\n{P:.6f}' )







