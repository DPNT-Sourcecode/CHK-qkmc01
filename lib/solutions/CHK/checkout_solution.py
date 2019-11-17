

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    for item in skus:
        if item not in price_map.keys():
            return -1

    running_total = 0
    for item in skus:
        running_total += price_map[item]

    num_product_a = skus.count('A')
    num_a_discounts = round(num_product_a / 3 if num_product_a >= 3 else 0)
    a_discount = (num_a_discounts * 20)

    num_product_b = skus.count('B')
    num_b_discounts = round(num_product_b / 2 if num_product_b >= 2 else 0)
    b_discount = (num_b_discounts * 15)

    return running_total - a_discount - b_discount



