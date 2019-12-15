import funkcje

def test_dodawanie():
    assert funkcje.dodawanie(5, 5) == 10
    assert funkcje.dodawanie(2, -1) == 1
    assert funkcje.dodawanie(4.3, 5.6) - 9.9 < 0.0000001

def test_product():
    assert funkcje.product(5, 5) == 5
    assert funkcje.product(-2, 3) == -6
    assert funkcje.product(2.5, 2) == 5
    assert funkcje.product(0, 0) == 0

def test_palindrom():
    assert funkcje.palindrom("madam")
    assert funkcje.palindrom("ala")
