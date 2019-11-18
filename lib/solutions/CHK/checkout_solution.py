

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
        'U': [(4, 40)],
        'V': [(3, 20), (2, 10)],
    }

    skus = list(skus)

    for item in skus:
        if item not in price_map.keys():
            return -1

    running_total = 0


    def process_item_code(skus_, code):
        discounts = discount_map[code]
        total_discount = 0

        num_discountable_products = skus_.count(code)
        total_for_items = num_discountable_products + price_map[code]
        for discount in discounts:
            quantity_qualifier = discount[0]
            num_discounts = int(num_discountable_products / quantity_qualifier)
            num_discountable_products = int(num_discountable_products % quantity_qualifier)
            if num_discounts:
                if isinstance(discount[1], int):
                    total_discount += num_discounts * discount[1]
                else:
                    for _ in range(num_discounts):
                        try:
                            skus.remove(discount[1])
                        except ValueError:
                            pass
        breakpoint()
        return total_for_items - total_discount


    for code in discount_map.keys():
        running_total += process_item_code(skus, code)

    for item in skus:
        running_total += price_map[item]

    return running_total

