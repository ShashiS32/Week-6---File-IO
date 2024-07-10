with open("names.txt" , "r") as skib:
    for line in skib:
        print("Hello" , line.rstrip())