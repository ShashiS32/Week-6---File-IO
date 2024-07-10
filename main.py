name = []

with open("files.txt") as skib:
    for line in skib:
        name.append(line.rstrip)

for names in sorted(name):
    print(f"Hello {names}")