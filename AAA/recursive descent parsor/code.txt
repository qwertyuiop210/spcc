# Recursive Descent Parser for grammar:
# E  -> T E'
# E' -> + T E' | ε
# T  -> F T'
# T' -> * F T' | ε
# F  -> (E) | i

SUCCESS = True
FAILED = False

cursor = 0
string = ""


def E():
    global cursor
    print(f"{string[cursor:]:<16} E -> T E'")
    if T():
        if Edash():
            return SUCCESS
    return FAILED


def Edash():
    global cursor
    if cursor < len(string) and string[cursor] == '+':
        print(f"{string[cursor:]:<16} E' -> + T E'")
        cursor += 1
        if T():
            if Edash():
                return SUCCESS
        return FAILED

    print(f"{string[cursor:]:<16} E' -> ε")
    return SUCCESS


def T():
    global cursor
    print(f"{string[cursor:]:<16} T -> F T'")
    if F():
        if Tdash():
            return SUCCESS
    return FAILED


def Tdash():
    global cursor
    if cursor < len(string) and string[cursor] == '*':
        print(f"{string[cursor:]:<16} T' -> * F T'")
        cursor += 1
        if F():
            if Tdash():
                return SUCCESS
        return FAILED

    print(f"{string[cursor:]:<16} T' -> ε")
    return SUCCESS


def F():
    global cursor

    if cursor < len(string) and string[cursor] == '(':
        print(f"{string[cursor:]:<16} F -> ( E )")
        cursor += 1

        if E():
            if cursor < len(string) and string[cursor] == ')':
                cursor += 1
                return SUCCESS
        return FAILED

    elif cursor < len(string) and string[cursor] == 'i':
        print(f"{string[cursor:]:<16} F -> i")
        cursor += 1
        return SUCCESS

    return FAILED


# -----------------------------
# MAIN
# -----------------------------
string = input("Enter the string: ")
cursor = 0

print("\nInput\t\tAction")
print("---------------------------------")

if E() and cursor == len(string):
    print("---------------------------------")
    print("String is successfully parsed")
else:
    print("---------------------------------")
    print("Error in parsing String")