name = input("Whats ur name? ")

file = open("names.txt" , "w" )

file.write(name)

file.close