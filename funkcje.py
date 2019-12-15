import math

def dodawanie(x, y):
    return x + y

def product(x, y):
    return x * y

def palindrom(napis):
    return napis.lower().replace(" ","") == napis[::-1].lower().replace(" ","")

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")

    return math.pi * r**2
