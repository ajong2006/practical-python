# pcost.py
#
# Exercise 2.17
import csv
import sys


def portfolio_cost(filename):

    file = open(filename, encoding="utf8")
    rows = csv.reader(file)
    headers = next(rows)
    print('Headers: ', headers)

    total_cost = 0

    for n, row in enumerate(rows):
        try:
            total_cost = total_cost + int(row[1]) * float(row[2])
        except ValueError:
            print(f"Row {n}: Couldn't convert: {row}")

    return total_cost


if len(sys.argv) == 2:
    csv_name = sys.argv[1]
else:
    csv_name = './Data/missing.csv'

cost = portfolio_cost(csv_name)
print('Total Cost: ', cost)
