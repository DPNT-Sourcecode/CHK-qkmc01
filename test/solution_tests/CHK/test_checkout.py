from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout('ABCD') == 115


def test_checkout_multiples():
    assert checkout_solution.checkout('ABCDBA') == 180


def test_checkout_discount_times_1():
    assert checkout_solution.checkout('AAA') == 130


def test_checkout_discount_plus_1():
    assert checkout_solution.checkout('AAAA') == 180

def test_checkout_fives_As():
    assert checkout_solution.checkout('AAAAA') == 230

def test_checkout_three_Bs():
    assert checkout_solution.checkout('BBB') == 75

def test_checkout_discount_times_2():
    assert checkout_solution.checkout('AAAAAA') == 260


def test_checkout_discount_b_times_1():
    assert checkout_solution.checkout('BB') == 45

def test_checkout_lower_case_rejected():
    assert checkout_solution.checkout('a') == -1

def test_bad_chars_rejected():
    assert checkout_solution.checkout('-') == -1
