from sympy import symbols, diff

def user_defined_function(x):
    return eval(expression_str)

def newton_raphson_method(init_x, f, f_prime, f_double_prime, max_iterations=100):
    iteration = 0
    for iteration in range(max_iterations):
        newton_m = init_x - f_prime / f_double_prime
        init_x = newton_m

    return newton_m, iteration

if __name__ == "__main__":
    x = symbols('x')

    
    expression_str = input("Enter the expression in terms of x: ")
    f = user_defined_function  

    
    init_x = float(input("Enter the number to initialize:"))

    
    f_prime = diff(f(x), x)
    f_double_prime = diff(f_prime, x)

    
    newton_result, iterations_done = newton_raphson_method(init_x, f(init_x), f_prime.subs(x, init_x), f_double_prime.subs(x, init_x), max_iterations)

    print("The expression:", expression_str)
    print("The single derivative:", f_prime)
    print("The Double derivative:", f_double_prime)
    print(f"The Newton method applied for f (after {iterations_done} iterations):", newton_result)
