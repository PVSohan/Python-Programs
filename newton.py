import sympy as sp
import matplotlib.pyplot as plt

def newtonmethod(init,exp,pre):
    x = sp.symbols('x')
    fx = sp.sympify(exp)
    f_prime = sp.diff(fx,x)
    f_double_prime = sp.diff(f_prime,x)
    xvalues = [init]
    xvalue = init
    xold = None
    iterate = 0
    
    while xold is None or round(xvalue,pre) != round(xold,pre):
        xold = xvalue
        xvalue = xvalue - f_prime.subs(x , xvalue)/f_double_prime.subs(x , xvalue)
        iterate +=1
        xvalues.append(xvalue)
        print(f"Iteration{iterate}: x = {round(xvalue,pre)}")
        
    return xvalues

exp = input("Enter the function expression(in terms x):")
Start = float(input("Enter the starting index:"))
End = float(input("Enter the last index:"))
init_g =(Start+End)/2
pre = int(input("Enter your precision:"))
newtonmethod(init_g,exp,pre)

