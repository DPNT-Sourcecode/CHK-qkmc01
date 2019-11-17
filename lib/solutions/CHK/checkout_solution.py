

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
    return running_total

