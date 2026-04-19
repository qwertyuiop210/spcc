MAX = 100

# MNT structure
class MNTEntry:
    def __init__(self, name, mdt_index):
        self.name = name
        self.mdt_index = mdt_index


mnt = []
mdt = []
intermediate = []   # ✅ store intermediate code


# Search parameter in ALA
def search_ala(param, ala_list):
    for i in range(len(ala_list)):
        if ala_list[i] == param:
            return i
    return -1


# Main Program
n = int(input("Enter number of lines:\n"))

print("Enter source program:")
lines = [input() for _ in range(n)]

i = 0
while i < n:
    parts = lines[i].strip().split()

    if len(parts) == 0:
        i += 1
        continue

    word1 = parts[0]

    # Check MACRO
    if word1 == "MACRO":
        i += 1
        proto_parts = lines[i].strip().split()

        name = proto_parts[0]
        params = proto_parts[1] if len(proto_parts) > 1 else ""

        # Store in MNT
        mnt.append(MNTEntry(name, len(mdt)))

        # Process parameters into ALA
        ala_local = params.split(',') if params else []

        # Store prototype in MDT
        mdt.append(f"{name} {params}")

        # Process macro body
        while True:
            i += 1
            line = lines[i]

            if "MEND" in line:
                mdt.append("MEND")
                break

            temp = ""
            tokens = line.replace(',', ' ').split()

            for tok in tokens:
                index = search_ala(tok, ala_local)

                if index != -1:
                    temp += f"#{index} "
                else:
                    temp += tok + " "

            mdt.append(temp.strip())

    else:
        # ✅ Store instead of print
        intermediate.append(lines[i])

    i += 1


# ✅ PRINT OUTPUT PROPERLY

print("\nIntermediate Code:")
for line in intermediate:
    print(line)

print("\nMDT (Macro Definition Table):")
for idx, line in enumerate(mdt):
    print(f"{idx}\t{line}")

print("\nMNT (Macro Name Table):")
for idx, entry in enumerate(mnt):
    print(f"{idx}\t{entry.name}\t{entry.mdt_index}")