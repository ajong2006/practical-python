# pcost.py
#
# Exercise 1.31

def portfolio_cost(filename):

    file = open(filename,'rt', encoding="utf8")
    headers = next(file).split(',')
    total_cost = 0

    for line in file:
        try:
            row = line.split(',')
            total_cost = total_cost + int(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't parse", line)
                    
    return total_cost

cost = portfolio_cost('./Data/missing.csv')
print('Total Cost: ', cost)
