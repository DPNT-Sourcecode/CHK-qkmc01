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
"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""

@pytest.mark.parametrize("product_skus, expected", [
    ('HH', 20),
    ('HHHHH', 45),
    ('HHHHHHHHHH', 80),
    ('KK', 150),
    ('KKK', 230),
    ('NNN', 120),
    ('NNNM', 120),
    ('NNNMM', 135),
    ('PPPP', 200),
    ('PPPPP', 200),
    ('QQ', 60),
    ('QQQ', 80),
    ('RRR', 150),
    ('RRRQ', 150),
    ('RRRQQQ', 210),
    ('RRRQQQQ', 230),

])
def test_remaining_offers(product_skus, expected):
    assert checkout_solution.checkout(product_skus) == expected

def test_checkout():
    assert checkout_solution.checkout('ABCD') == 115

def test_checkout_multiples():
    assert checkout_solution.checkout('ABCDBA') == 180



