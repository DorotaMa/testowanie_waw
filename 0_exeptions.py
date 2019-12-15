import math

# def circle_area(r):
#     if type(r) not in [int, float]:
#         return "Podałeś nieprawidłową typ. Podaj liczbę"
#     elif r < 0:
#         return "Koło o takim promieniu nie istnieje"
#     else:
#         return math.pi*r**2
#
#
# print(circle_area(3))
# print(circle_area(1))
# print(circle_area(0))
# print(circle_area(-3))
# print(circle_area(2+5j))
# print(circle_area(True))
# print(circle_area("asd"))

def circle_area(r):

    try:
        if r < 0:
            raise Exception("Promień nie może być ujemny")
        return math.pi*r**2
    except:
        return "Coś poszło nie tak"



print(circle_area(3))
print(circle_area(1))
print(circle_area(0))
print(circle_area(-3))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area("asd"))
