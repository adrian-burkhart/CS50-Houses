import csv
from sys import argv
from cs50 import SQL


if (len(argv) != 2):  # Checks for correct usage
    print("usage error, python import.py characters.csv")
    exit()

open("students.db", "w").close()

db = SQL("sqlite:///students.db")

# Create a table called students in database file called students.db
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC);")

students_list = []
with open(argv[1]) as csv_file:  # read students from file
    reader = csv.DictReader(csv_file)
    for row in reader:
        x = row["name"].split()
        if (len(x) == 2):
            first = x[0]
            middle = None
            last = x[1]
        else:
            first = x[0]
            middle = x[1]
            last = x[2]

        house = row["house"]
        birth = row["birth"]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?);", first, middle, last, house, birth)