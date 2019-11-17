

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price_map = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
    }

    discount_map = {
        'A': [(5, 50), (3, 20)],
        'B': [(2, 15)],
        'C': [],
        'D': [],
        'E': [(2, 'B')],
        'F': [(3, 10)],
    }

    skus = list(skus)

    for item in skus:
        if item not in price_map.keys():
            return -1



    def calc_discount(skus_, code, discounts):
        total_discount_for_item = 0

        num_discountable_products = skus_.count(code)
        for discount in discounts:
            num_discounts = int(num_discountable_products / discount[0])
            num_discountable_products = int(num_discountable_products % discount[0])
            if isinstance(discount[1], int):
                total_discount_for_item += num_discounts * discount[1]
            else:
                try:
                    skus.remove(discount[1])
                except ValueError:
                    pass
        return total_discount_for_item

    e_discount = calc_discount(skus, 'E', discount_map['E'])
    f_discount = calc_discount(skus, 'F', discount_map['F'])
    a_discount = calc_discount(skus, 'A', discount_map['A'])
    b_discount = calc_discount(skus, 'B', discount_map['B'])

    running_total = 0
    for item in skus:
        running_total += price_map[item]

    breakpoint()

    return running_total - a_discount - b_discount - f_discount - e_discount






