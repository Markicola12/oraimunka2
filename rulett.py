import random
import os

tipp = int(input("Tippelj egy egész számot 1 és 6 között: "))

szam = random.randint(1,6)

if tipp == szam:
    print("Nyertél!")

