import math
import cmath
import inspect
import difflib

class MathFunctions:
    @staticmethod
    def addition(*args):
        return sum(args)
    
    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def exponentiation(base, exp):
        return base ** exp

    @staticmethod
    def pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
    
    @staticmethod
    def sine_rule(a, A, B):
        return (a / math.sin(math.radians(A))) * math.sin(math.radians(B))
    
    @staticmethod
    def cosine_rule(a, b, C):
        return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))

    @staticmethod
    def sine(angle):
        return math.sin(math.radians(angle))
    
    @staticmethod
    def cosine(angle):
        return math.cos(math.radians(angle))
    
    @staticmethod
    def tangent(angle):
        return math.tan(math.radians(angle))

    @staticmethod
    def to_radians(degrees):
        return math.radians(degrees)
    
    @staticmethod
    def to_degrees(radians):
        return math.degrees(radians)

    @staticmethod
    def quadratic_formula(a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return root1, root2

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    @staticmethod
    def combinations(n, r):
        return math.comb(n, r)

    @staticmethod
    def permutations(n, r):
        return math.perm(n, r)

    @staticmethod
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    @staticmethod
    def vector_magnitude(vector):
        return math.sqrt(sum(comp**2 for comp in vector))

    @staticmethod
    def dot_product(vector1, vector2):
        return sum(a * b for a, b in zip(vector1, vector2))

    @staticmethod
    def logarithm(value, base=math.e):
        if base == 10:
            return math.log10(value)
        return math.log(value, base)

def print_methods(cls):
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    for name, func in methods:
        sig = inspect.signature(func)
        print(f"{name}{sig}")

def find_matches(input_name, cls):
    methods = [name for name, _ in inspect.getmembers(cls, predicate=inspect.isfunction)]
    exact_matches = [name for name in methods if name.startswith(input_name)]
    close_matches = difflib.get_close_matches(input_name, methods, n=5, cutoff=0.1)
    matches = list(set(exact_matches + close_matches))
    return matches

def get_method_names(cls):
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    return [name for name, _ in methods]

def main():
    print("Available functions:")
    print_methods(MathFunctions)
    
    selected_function = input("Select a function: ")
    if not selected_function in get_method_names(MathFunctions):
        matches = find_matches(selected_function, MathFunctions)
        
        if not matches:
            print("No matches found.")
            return

        print("Did you mean:")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match}")
        
        choice = int(input("Enter the number of the function you want to use: ")) - 1
        selected_function = matches[choice]

    params = input("Enter the parameters separated by commas: ")
    
    try:
        if 'vector' in selected_function:
            params = [list(map(float, param.split())) for param in params.split(';')]
        else:
            params = [float(param) for param in params.split(',')]
        result = getattr(MathFunctions, selected_function)(*params)
        print(f"Result: {result}")
    except AttributeError:
        print("Function not found.")
    except TypeError:
        print("Invalid parameters for the function.")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
