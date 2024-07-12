import csv
name = input("Name?: ")
home = input("Wheres ur home?: ")

with open("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name" , "home"])
    writer.writerow({"name":name, "home":home})