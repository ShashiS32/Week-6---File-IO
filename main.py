names = []

with open("names.txt") as skib:
    for line in skib:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")