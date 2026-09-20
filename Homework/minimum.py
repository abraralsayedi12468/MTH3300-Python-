#******************************************************************************
# minimum.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Remarks (optional):
#
#
#


# This holds the answer to the question "Should we keep guessing?"
# In the beginning, we certainly should
 # inputs
c0 = float(input("Enter x^0 coefficient: "))
c1 = float(input("Enter x^1 coefficient: "))
c2 = float(input("Enter x^2 coefficient: "))
c3 = float(input("Enter x^3 coefficient: "))
x = float(input("Enter guess x_0: "))

D = 4*x**3 + 3*c3*x**2 + 2*c2*x + c1

while abs(D) > 0.000001:
    Dp = 12*x**2 + 6*c3*x + 2*c2
    x = x - D / Dp
    D = 4*x**3 + 3*c3*x**2 + 2*c2*x + c1

p = x**4 + c3*x**3 + c2*x**2 + c1*x + c0

print("x =", x)
print("min value =", p)