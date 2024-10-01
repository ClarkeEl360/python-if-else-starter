import random
import time
points = 0



while points < 100:
    a = random.randint(1, 6)

    if a == 1:
        print("Your aliens color was red. +15 points")
        points = points + 15
    if a == 2:
        print("Your aliens color was orange. +10 points")
        points = points + 10
    if a == 3:
        print("Your aliens color was yellow. +20 points")
        points = points + 20
    if a == 4:
        print("Your aliens color was green. +30 points")
        points = points + 30
    if a == 5:
        print("Your aliens color was blue. -5 points")
        points = points - 5
    if a == 6:
        print("Your aliens color was purple. -10 points")
        points = points - 10

    time.sleep(2)
    if points < 100:
        print(f"You cerently have, {points}, points.")
    else:
        print(f"You won with, {points}, points!!")
    time.sleep(2)