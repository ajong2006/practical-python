"""
bounce.py
Exercise 1.5
"""

BOUNCE = 0
HEIGHT = 100

while BOUNCE <=10:
    print(BOUNCE, round(HEIGHT, 4))
    HEIGHT = HEIGHT * (3/5)
    BOUNCE = BOUNCE +1
    