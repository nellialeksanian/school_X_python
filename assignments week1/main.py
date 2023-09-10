def test_positive():
    assert nod(10, 5) == 5, "nod(10, 5) should be 5"
    assert nod(10, 50) == 10, "nod(10, 50) should be 10"
    assert nod(15, 27) == 3, "nod(15, 27) should be 3"
    assert nod(6, 14) == 2, "nod(6, 14) should be 2"
    assert nod(150, 120) == 30, "nod(150, 120) should be 30"
    assert nod(17, 120) == 1, "nod(17, 120) should be 1"


def test_negative():
    assert nod(0, 5) == 0, "Testing 0 failed..."
    assert nod(3, 0) == 0, "Testing 0 failed..."
    assert nod(0, 0) == 0, "Testing 0 failed..."
    assert nod(1, 0) == 0, "Testing 0 failed..."
    assert nod(0, 1) == 0, "Testing 0 failed..."
    assert nod(-1, 1) == 0, "Testing negative failed..."
    assert nod(-17, 17) == 0, "Testing negative failed..."
    assert nod(-22, -25) == 0, "Testing negative failed..."
    assert nod(0.5, 0.5) == 0, "Testing not natural failed..."
    assert nod(1, 0.5) == 0, "Testing not natural failed..."
    assert nod(10, 0.5) == 0, "Testing not natural failed..."
    assert nod(10.7, 355) == 0, "Testing not natural failed..."


def nod(number_1: int, number_2: int) -> int:
    if not isinstance(number_1, int) or not isinstance(number_2, int) or number_1 <= 0 or number_2 <= 0:
        return 0
    while number_1 != 0 and number_2 != 0:
        if number_1 >= number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_1 or number_2


if __name__ == "__main__":
    test_positive()
    test_negative()
    print("Everything passed")



