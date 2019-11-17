from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout('ABCD') == 115


def test_checkout_multiples():
    assert checkout_solution.checkout('ABCDBA') == 195


def test_checkout_discount_times_1():
    assert checkout_solution.checkout('AAA') == 130


def test_checkout_discount_plus_1():
    assert checkout_solution.checkout('AAAA') == 180


def test_checkout_discount_times_2():
    assert checkout_solution.checkout('AAAAAA') == 260


def test_checkout_discount_b_times_1():
    assert checkout_solution.checkout('BB') == 45

def test_checkout_lower_case_accepted():
    assert checkout_solution.checkout('a') == 50
