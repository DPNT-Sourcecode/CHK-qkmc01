

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

    running_total = 0
    for item in skus:
        running_total += price_map[item]





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


    ##############################################################################
    # handle product E
    ##############################################################################
    e_discount = calc_discount(skus, 'E', discount_map['E'])

    ##############################################################################
    # handle product F
    ##############################################################################
    f_discount = calc_discount(skus, 'F', discount_map['F'])

    ##############################################################################
    # handle product A
    ##############################################################################
    a_discount = calc_discount(skus, 'A', discount_map['A'])


    ##############################################################################
    # handle product B
    ##############################################################################
    num_product_b = skus.count('B')
    # assuming free B's cant be used in subsequent discounts
    # this may be wrong given the requirement that the
    # customer is always right!
    # num_product_b -= num_free_bs
    num_product_b = max(num_product_b, 0)
    num_b_discounts = int(num_product_b / 2)
    b_discount = (num_b_discounts * 15) # + (num_free_bs * 30)


    return running_total - a_discount - b_discount - f_discount - e_discount




