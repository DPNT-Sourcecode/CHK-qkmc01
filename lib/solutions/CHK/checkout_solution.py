

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
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        'Y': 20,
        'Z': 21,
    }

    # discounts that affect other products must come first
    discount_map = {
        'E': [(2, 'B')],  # buy 2, get free B
        'N': [(3, 'M')],
        'R': [(3, 'Q')],
        'A': [(5, 50), (3, 20)], # buy 5, get 50 discount / buy 3, get 20 discount
        'B': [(2, 15)],
        'F': [(3, 10)],
        'H': [(10, 20), (5, 5)],
        'K': [(2, 20)],
        'P': [(5, 50)],
        'Q': [(3, 10)],
        'U': [(4, 40)],
        'V': [(3, 20), (2, 10)],
    }

    skus = list(skus)

    for item in skus:
        if item not in price_map.keys():
            return -1

    skus = sorted(skus, key=lambda x: price_map[x], reverse=True)


    def process_item_code(skus_, code):
        discounts = discount_map[code]
        total_discount = 0

        num_discountable_products = skus_.count(code)
        total_for_items = num_discountable_products * price_map[code]
        for discount in discounts:
            quantity_qualifier = discount[0]
            discount_target = discount[1]

            num_discounts = int(num_discountable_products / quantity_qualifier)
            num_discountable_products = int(num_discountable_products % quantity_qualifier)
            if num_discounts:
                total_discount = apply_discount(discount_target, num_discounts,
                                                total_discount)
        for item in range(skus_.count(code)):
            skus.remove(code)

        return total_for_items - total_discount


    def apply_discount(discount_target, num_discounts, total_discount):
        if isinstance(discount_target, int):
            total_discount += num_discounts * discount_target
        else:
            for _ in range(num_discounts):
                try:
                    skus.remove(discount_target)
                except ValueError:
                    pass
        return total_discount


    def apply_any_3_deal():
        matching_skus = []
        offer_hit = []
        for sku in skus:
            if sku in ['S', 'T', 'X', 'Y', 'Z']:
                matching_skus.append(sku)
                if len(matching_skus) == 3:
                    offer_hit.append(matching_skus)
                    matching_skus = []

        running_total = 0
        for hit in offer_hit:
            for item in hit:
                skus.remove(item)
            running_total += 45

        return running_total

    running_total = apply_any_3_deal()

    for code in discount_map.keys():
        running_total += process_item_code(skus, code)


    for item in skus:
        running_total += price_map[item]

    return running_total





