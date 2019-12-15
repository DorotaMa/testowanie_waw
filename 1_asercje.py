# def dzielenie(a,b):
#     return a/b
#
#
# if dzielenie(10, 5) ==2:
#     print("Passed")
# else:
#     raise Exception("FAILED")
#
# if dzielenie(10, 2) ==3:
#     print("Passed")
# else:
#     raise Exception("FAILED")
#
#
# print(dzielenie(10,1)==2)
#
# assert div(10, 5) == 2, "FAILED"
# print("PASSED")
# assert div(10, 2) == 5, "FAILED"
# print("PASSED")

#
# def kwadrat_sumy(a, b):
#     return (a + b)**2
#
# assert kwadrat_sumy(1,1) == 4, "FALILED"
# print("PASSED")
# assert kwadrat_sumy(2,2) == 80, "FALILED"
# print("PASSED")


# Asercje nie służą tylko do testowania

# def div(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Nie można dzielić przez zero.")
#
# div(5, 0)

# def div (a, b):
#     assert b != 0, "Nie można dzielić przez zero"
#     return a/b
# div(5, 0)

def konkatenacja (str1, str2):
    return str1 + " " + str2

assert konkatenacja("aaa","bbb") =="aaa bbb", "FAILED"
assert konkatenacja("qwe","asd") =="qwe asd", "FAILED"
assert konkatenacja("","") ==" ", "FAILED"