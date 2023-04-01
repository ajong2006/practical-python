# pcost.py
#
# Exercise 1.32
import csv

def portfolio_cost(filename):

    file = open(filename, encoding="utf8")
    rows = csv.reader(file)
    headers = next(rows)
    print('Headers: ', headers)

    total_cost = 0

    for row in rows:
        try:
            total_cost = total_cost + int(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't parse", row)
           
    return total_cost

cost = portfolio_cost('./Data/missing.csv')
print('Total Cost: ', cost)
