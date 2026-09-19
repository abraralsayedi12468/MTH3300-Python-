#******************************************************************************
# invest.py
#******************************************************************************
# Name: Abrar Alsayedi
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://chatgpt.com/share/6a5b0fac-96f4-83ea-ae7f-c3385b0eb3eb
#I used chatgbt for minor questions to get my math right 
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 
import math 
a = input('Enter C for continuous or N for noncontinuous: ')

if a == 'C':
    x = True # this is so that i can can later add an if statment to update p 
    p = float(input('Enter the initial amount: '))
    t1 = float(input('Enter the first time period in years: '))
    k1 = float(input('Enter the first growth rate as a percentage: '))
    con1 = p * math.exp((k1/100)*t1)
    if x == True:
        p = con1
        t2 = float(input('Enter the second time period in years: '))
        k2 = float(input('Enter the second growth rate as a percentage: '))
        con2 = p * math.exp((k2/100)*t2)
        print(f'The ending value is{con2 : .2f}' )
        
elif a == 'N':
    x = True 
    p = float(input('Enter the initial amount: '))
    t1 = float(input('Enter the first time period in years: '))
    r1 = float(input('Enter the first growth rate as a percentage: '))
    n1 = float(input('Enter the number of times compounded per year: '))
    nom1 = p * (1 + ((r1/100)/n1))**(n1*t1)
    if x == True: 
        p = nom1 
        t2 = float(input('Enter the second time period in years: '))
        r2 = float(input('Enter the second growth rate as a percentage: '))
        n2 = float(input('Enter the number of times compounded per year: '))
        nom2 = p * (1 + ((r2/100)/n2))**(n2*t2)
        print(f'The ending value is{nom2 : .2f}' )
        