

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }

    for item in skus:
        if item not in price_map.keys():
            return -1

    running_total = 0
    for item in skus:
        running_total += price_map[item]

    num_product_e = skus.count('E')
    num_free_bs = int(num_product_e / 2)

    breakpoint()

    num_product_a = skus.count('A')
    num_a_buy_5_discounts = int(num_product_a / 5)
    remaining_as = num_product_a % 5
    num_a_buy_3_discounts = int(remaining_as / 3)
    a_discount = (num_a_buy_5_discounts * 50) + (num_a_buy_3_discounts * 20)

    num_product_b = skus.count('B')
    # assuming free B's cant be used in subsequent discounts
    # this may be wrong given the requirement that the
    # customer is always right!
    num_product_b -= num_free_bs
    num_b_discounts = int(max(num_product_b, 0) / 2)
    b_discount = (num_b_discounts * 15)


    return running_total - a_discount - b_discount

