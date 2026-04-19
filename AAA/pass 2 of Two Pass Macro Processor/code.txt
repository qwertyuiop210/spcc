#Design & Implementation of Pass 2 of Two Pass Macro Processor
MAX = 100

# MNT structure
class MNTEntry:
    def __init__(self, name, mdt_index):
        self.name = name
        self.mdt_index = mdt_index


mnt = []
mdt = []
ala = []


# ---- INPUT MNT ----
mntc = int(input("Enter number of entries in MNT:\n"))

print("Enter MNT (name and MDT index):")
for _ in range(mntc):
    name, index = input().split()
    mnt.append(MNTEntry(name, int(index)))

# ---- INPUT MDT ----
mdtc = int(input("Enter number of entries in MDT:\n"))

print("Enter MDT entries:")
for _ in range(mdtc):
    mdt.append(input())

# ---- INPUT INTERMEDIATE CODE ----
n = int(input("Enter number of lines in intermediate code:\n"))

print("Enter intermediate code:")
lines = [input() for _ in range(n)]

print("\nExpanded Code:")

for line in lines:
    parts = line.strip().split()

    if len(parts) == 0:
        continue

    opcode = parts[0]
    operands = parts[1] if len(parts) > 1 else ""

    found = -1

    # Search MNT
    for j in range(len(mnt)):
        if opcode == mnt[j].name:
            found = j
            break

    if found != -1:
        # Macro call found

        # Setup ALA
        ala_local = operands.split(',') if operands else []

        mdtp = mnt[found].mdt_index + 1

        # Expand macro
        while True:
            if "MEND" in mdt[mdtp]:
                break

            tokens = mdt[mdtp].split()
            result = ""

            for tok in tokens:
                if tok.startswith('#'):
                    index = int(tok[1])
                    result += ala_local[index] + " "
                else:
                    result += tok + " "

            print(result.strip())
            mdtp += 1

    else:
        # Not a macro call
        print(line)