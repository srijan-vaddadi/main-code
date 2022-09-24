# Program prints records in tblTemps in database CityTemperatures.db

import sqlite3

conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()

# prints the data as a collection of tuples
for row in cursor.execute('SELECT * FROM tblTemps WHERE temperature >= 20 ORDER BY temperature DESC'):
    city, temperature, localTime = row
    print(row)
print("\n\n")

# This prints the data in neat columns
# It also shows a different way of defining the for loop condition
# and the records are displayed in the sequence of city

# print headings
print("%-15s%20s%20s" % ("City", "Temperature", "Local time"))
sql = cursor.execute('SELECT * FROM tblTemps ORDER BY city')

for row in sql:
    city, temperature, localTime = row
    print("%-15s %15d %20s" % (city, temperature, localTime))

input("\nPress Enter to exit: ")
