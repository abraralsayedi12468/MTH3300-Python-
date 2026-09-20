#******************************************************************************
# ttable.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Remarks (optional):
#
#
#


    
# TEST VALUES FOR YOUR FUNCTION f()

import math

def f(x):
    return ((9 * 7 * 5 * 3) / (2 * math.sqrt(10) * 8 * 6 * 4 * 2)) * (1 + (x**2) / 10) ** (-11 / 2)

A = float(input('Enter Value A: '))
N = int(input('Enter int N: '))

delta_x = (100 - A) / N
total = 0

for i in range(N + 1):
    x = A + i * delta_x

    if i == 0 or i == N:
        total += f(x)
    else:
        total += 2 * f(x)

value = (delta_x / 2) * total

print(f"VALUE: {value:.6f}")