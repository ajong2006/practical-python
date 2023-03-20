""" 
mortgage.py
Exercise 1.10
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if num_months > extra_payment_start_month and num_months < extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
        num_months = num_months + 1
        print('Month:', num_months, 'Total paid:', total_paid, 'Principal:', principal)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        num_months = num_months + 1 
        print('Month:', num_months, 'Total paid:', total_paid, 'Principal:', principal)

print('Total paid:', total_paid)
print('Number of months:', num_months)
