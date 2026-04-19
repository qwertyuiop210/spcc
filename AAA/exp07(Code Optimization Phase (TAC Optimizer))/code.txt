# Code Optimization Phase (TAC Optimizer)

class TAC:
    def __init__(self, result, arg1, op, arg2):
        self.result = result
        self.arg1 = arg1
        self.op = op
        self.arg2 = arg2


code = []


# Display TAC
def display(title):
    print(f"\n{title}")
    print("Three Address Code:")
    for c in code:
        if c.op == '=':
            print(f"{c.result} = {c.arg1}")
        else:
            print(f"{c.result} = {c.arg1} {c.op} {c.arg2}")


# Check if number
def is_number(x):
    return x.isdigit()


# ---------------- OPTIMIZATIONS ---------------- #

# 1. Constant Folding
def constant_folding():
    for c in code:
        if is_number(c.arg1) and is_number(c.arg2):
            a = int(c.arg1)
            b = int(c.arg2)

            if c.op == '+':
                res = a + b
            elif c.op == '-':
                res = a - b
            elif c.op == '*':
                res = a * b
            elif c.op == '/':
                res = a // b if b != 0 else 0
            else:
                continue

            c.arg1 = str(res)
            c.arg2 = ""
            c.op = '='


# 2. Common Subexpression Elimination
def common_subexpression():
    for i in range(len(code)):
        for j in range(i + 1, len(code)):
            if (code[i].arg1 == code[j].arg1 and
                code[i].arg2 == code[j].arg2 and
                code[i].op == code[j].op):

                code[j].arg1 = code[i].result
                code[j].arg2 = ""
                code[j].op = '='


# 3. Dead Code Elimination
def dead_code_elimination():
    i = 0
    while i < len(code):
        used = False

        for j in range(i + 1, len(code)):
            if (code[i].result == code[j].arg1 or
                code[i].result == code[j].arg2):
                used = True
                break

        if not used:
            code.pop(i)
        else:
            i += 1


# ---------------- MAIN ---------------- #

n = int(input("Enter number of statements: "))

print("Enter TAC (format: result arg1 op arg2)")
print("Example: t1 2 + 3\n")

for _ in range(n):
    parts = input().split()
    result, arg1, op, arg2 = parts
    code.append(TAC(result, arg1, op, arg2))

display("--- BEFORE OPTIMIZATION ---")

constant_folding()
common_subexpression()
dead_code_elimination()

display("--- AFTER OPTIMIZATION ---")