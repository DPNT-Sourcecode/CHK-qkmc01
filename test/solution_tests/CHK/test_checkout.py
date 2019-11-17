from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout('ABCD') == 115
    # multiples
    assert checkout_solution.checkout('ABCDBA') == 195
    # discount
    assert checkout_solution.checkout('AAA') == 130
    assert checkout_solution.checkout('AAAA') == 180
    assert checkout_solution.checkout('AAAAAA') == 260

