

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
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    # discounts that affect other products must come first
    discount_map = {
        'E': [(2, 'B')],
        'N': [(3, 'M')],
        'R': [(3, 'Q')],
        'A': [(5, 50), (3, 20)],
        'B': [(2, 15)],
        'F': [(3, 10)],
        'H': [(10, 20), (5, 5)],
        'K': [(2, 10)],
        'P': [(5, 50)],
        'Q': [(3, 10)],



    }

    skus = list(skus)

    for item in skus:
        if item not in price_map.keys():
            return -1


    def calc_discount(skus_, code):
        discounts = discount_map[code]
        total_discount_for_item = 0

        num_discountable_products = skus_.count(code)
        for discount in discounts:
            num_discounts = int(num_discountable_products / discount[0])
            num_discountable_products = int(num_discountable_products % discount[0])
            if num_discounts:
                if isinstance(discount[1], int):
                    total_discount_for_item += num_discounts * discount[1]
                else:
                    try:
                        skus.remove(discount[1])
                    except ValueError:
                        pass
        return total_discount_for_item

    total_discount = 0
    for code in discount_map.keys():
        total_discount += calc_discount(skus, code)


    running_total = 0
    for item in skus:
        running_total += price_map[item]

    return running_total - total_discount






