from sympy import symbols, parse_expr, Derivative
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

x = symbols('x')

expression = input("Expression: ")

eq = parse_expr(expression)
print(eq)

deq = Derivative(eq, x).doit()
print(deq)

a = float(input("Enter the left limit: "))
b = float(input("Enter the right limit: "))
acc = int(input("Enter the number of decimal places: "))
oa = a
ob = b
up = []
low = []
clist = []

while True:

    c = round((((deq.subs(x, b)) * a) - ((deq.subs(x, a)) * b)) / ((deq.subs(x, b) - (deq.subs(x, a)))), acc)

    low.append(a)
    up.append(b)
    clist.append(c)

    a = round(b, acc)
    b = round(c, acc)

    if round(a, acc) == round(b, acc):
        result = round(a, acc)
        break

data = {'Lower Limit': low,
        'Upper Limit': up,
        'Next Value': clist}
df = pd.DataFrame(data)

print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
print()
print(f"Minimizer of the function {expression} in the interval [{oa},{ob}] is {result}")


