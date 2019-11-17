from solutions.CHK import checkout_solution
import pytest

##############################################################################
# validation
##############################################################################
def test_checkout_lower_case_rejected():
    assert checkout_solution.checkout('a') == -1

def test_bad_chars_rejected():
    assert checkout_solution.checkout('-') == -1


##############################################################################
# products
##############################################################################
@pytest.mark.parametrize("product_skus, expected", [
    ('B', 30),
    ('BB', 45),
    ('BBB', 75),
])
def test_product_b(product_skus, expected):
    assert checkout_solution.checkout(product_skus) == expected

@pytest.mark.parametrize("product_skus, expected", [
    ('A', 50),
    ('AA', 100),
    ('AAA', 130),
    ('AAAA', 180),
    ('AAAAA', 200),
    ('AAAAAA', 250),
    ('AAAAAAA', 300),
    ('AAAAAAAA', 330),

])
def test_product_a(product_skus, expected):
    assert checkout_solution.checkout(product_skus) == expected


@pytest.mark.parametrize("product_skus, expected", [
    ('E', 40),
    ('EE', 80),
    ('EEB', 80),
    ('EEBB', 110),
])
def test_product_e(product_skus, expected):
    assert checkout_solution.checkout(product_skus) == expected


@pytest.mark.parametrize("product_skus, expected", [
    ('F', 10),
    ('FF', 20),
    ('FFF', 20),
    ('FFFF', 30),
    ('FFFFF', 40),
    ('FFFFFF', 40),
    ('FFFFFFF', 50),
])
def test_product_f(product_skus, expected):
    assert checkout_solution.checkout(product_skus) == expected

##############################################################################
# general
##############################################################################
def test_checkout():
    assert checkout_solution.checkout('ABCD') == 115

def test_checkout_multiples():
    assert checkout_solution.checkout('ABCDBA') == 180