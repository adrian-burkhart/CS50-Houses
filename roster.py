import csv
from sys import argv
from cs50 import SQL

if (len(argv) != 2):  # Checks for correct usage
    print("usage error, python import.py characters.csv")
    exit()

arg_house = argv[1]

open("students.db", "r").close()

db = SQL("sqlite:///students.db")

# Read from the database
list = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", arg_house)

for i in range(0, len(list)):
    if (list[i]['middle'] == None):
        print(f"{list[i]['first']} {list[i]['last']}, born {str(list[i]['birth'])}")
    else:
        print(f"{list[i]['first']} {list[i]['middle']} {list[i]['last']}, born {str(list[i]['birth'])}")