
with open("names.txt") as skib:
    for line in sorted(skib):
        print(f"Hello {line.rstrip}")
