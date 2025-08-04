import math

# Hardcoded coefficients
a = 1
b = -3
c = 2

# Discriminant
D = b**2 - 4*a*c

if D >= 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are:", root1, root2)
else:
    print("No real roots")
