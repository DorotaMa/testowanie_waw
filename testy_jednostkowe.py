def dodawanie(x, y):
    return x + y

# def test_dodawanie():
#     assert dodawanie(5, 5) == 10
#     assert dodawanie(2, -1) == 1
#     assert dodawanie(4.3, 5.6) == 9.6

# test_dodawanie()

def product(x, y):
    return x * y

def test_product():
    assert product(5, 5) == 25
    assert product(-2, 3) == -6
    assert product(2.5, 2) == 5
    assert product(0, 0) == 0
test_product()