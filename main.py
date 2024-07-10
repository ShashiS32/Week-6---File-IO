with open("names.txt" , "r") as skib:
    lines = skib.readlines()

for line in lines:
    print(f"hello" , line.rstrip()) 