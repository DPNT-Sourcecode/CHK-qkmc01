

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    items = [item.upper() for item in skus if item.upper() in price_map.keys()]
    running_total = 0
    for item in items:
        running_total += price_map[item]


    num_product_a = items.count('A')
    num_a_discounts = round(num_product_a / 3 if num_product_a >= 3 else 0)
    a_discount = (num_a_discounts * 20)

    num_product_b = items.count('B')
    num_b_discounts = round(num_product_b / 2 if num_product_b >= 2 else 0)
    b_discount = (num_b_discounts * 15)

    return running_total - a_discount - b_discount
