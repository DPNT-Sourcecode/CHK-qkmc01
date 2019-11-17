

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    items = list(skus)
    running_total = 0
    for item in items:
        running_total += price_map[item]


    num_product_a = items.count('A')
    num_a_discounts = round(num_product_a / 3 if num_product_a >= 3 else 0)
    return running_total - (num_a_discounts * 20)
