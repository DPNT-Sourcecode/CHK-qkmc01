from solutions.CHK import checkout_solution


def test_checkout():
    assert checkout_solution.checkout('ABC') == 123