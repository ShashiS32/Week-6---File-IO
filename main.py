name = input("Name: ")


with open("names.txt" , "a") as skib:

    skib.write(f"{name} \n")

