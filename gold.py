import math

def function(x):
    return x ** 3

def golden_section_search(left, right, iterations):
    golden_ratio = (1 + math.sqrt(5)) / 2
    epsilon = 1e-6  # Tolerance for the interval length

    x1 = right - (right - left) / golden_ratio
    x2 = left + (right - left) / golden_ratio

    for i in range(iterations):
        print(f"Iteration {i + 1}: Interval [{left}, {right}]")

        if function(x1) < function(x2):
            right = x2
            x2 = x1
            x1 = right - (right - left) / golden_ratio
        else:
            left = x1
            x1 = x2
            x2 = left + (right - left) / golden_ratio

    return (left + right) / 2

def main():
    left_bound = float(input("Enter the left bound of the interval: "))
    right_bound = float(input("Enter the right bound of the interval: "))
    iterations = int(input("Enter the number of iterations: "))

    result = golden_section_search(left_bound, right_bound, iterations)
    print(f"Minimum point is at x = {result}, f(x) = {function(result)}")

if __name__ == "__main__":
    main()


