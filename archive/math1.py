import sympy as sp
from itertools import product

def generate_equations(variables):
    equations = []

    # Generate equations with up to 2 squares of variables
    for degree in range(3):  # Up to degree 2 (including squares)
        for term in product(variables, repeat=degree):
            expression = sp.Mul(*term)
            equations.append(expression)

    return equations

def generate_all_expressions(variables):
    binary_operations = [sp.Add, sp.Mul, sp.Pow, sp.Pow, sp.Pow, sp.Pow]

    # Generate all possible expressions using binary operations
    expressions = []
    for op1, op2 in product(binary_operations, repeat=2):
        for var1, var2 in product(variables, repeat=2):
            expressions.append(op1(var1, op2(var2, 1)))  # Fix: Convert 'variables' to '1'

    return expressions

def check_equations(variables, target):
    all_variables = variables
    equations = generate_equations(all_variables)
    expressions = generate_all_expressions(all_variables)

    for eq in equations + expressions:
        current_value = eq.subs({var: 1 for var in all_variables})
        if sp.simplify(current_value) == target:
            return eq

    return None

# Define variables
x, y, z = sp.symbols('x y z')

# Specify target value
target_value = 42  # Adjust this as needed

# Check equations
equation = check_equations([x, y, z], target_value)

if equation:
    print("Found equation:", equation)
else:
    print("No equation found.")
