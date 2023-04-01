# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):

    file = open(filename,'rt', encoding="utf8")
    headers = next(file).split(',')
    total_cost = 0

    for line in file:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])

    return total_cost

cost = portfolio_cost('./Data/portfolio.csv')
print('Total Cost: ', cost)
