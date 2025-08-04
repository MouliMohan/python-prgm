import math

with open("input.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        a, b, c = map(float, line.strip().split())
        D = b**2 - 4*a*c
        print(f"Equation {line_num}: a={a}, b={b}, c={c}")
        if D >= 0:
            root1 = (-b + math.sqrt(D)) / (2*a)
            root2 = (-b - math.sqrt(D)) / (2*a)
            print("  Roots:", root1, root2)
        else:
            print("  No real roots")
