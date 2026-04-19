# Three Address Code Generator (Simple)

import string

def new_temp(count):
    return f"t{count}"


def generate_tac(expr):
    expr = list(expr)   # convert to list for easy modification
    temp_count = 1

    print("\nIntermediate Code (Three Address Code):")

    i = 0
    while i < len(expr):
        # Check operand
        if expr[i].isalnum():
            # Check operator
            if i + 2 < len(expr) and expr[i+1] in "+-*/":
                op1 = expr[i]
                op = expr[i+1]
                op2 = expr[i+2]

                temp = new_temp(temp_count)
                temp_count += 1

                print(f"{temp} = {op1} {op} {op2}")

                # Replace (op1 op op2) with temp
                expr = list(temp) + expr[i+3:]
                i = 0
                continue

        i += 1

    print(f"Result stored in: {''.join(expr)}")


# -----------------------------
# MAIN
# -----------------------------
expr = input("Enter a simple arithmetic expression: ")

# Basic validation
for ch in expr:
    if not (ch.isalnum() or ch in "+-*/"):
        print("Invalid character in expression.")
        exit()

generate_tac(expr)