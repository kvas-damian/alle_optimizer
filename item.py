from math import ceil

class Item(object):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def add_shiping_options(self, shipping_options):
        self.shipping_options = shipping_options

    def get_lowest_shipping_price(self, items_count):
        min_price = None

        for shipping_option in self.shipping_options:
            if shipping_option.postageFreeShipping:
                current_price = 0
            else:
                parcels_count = ceil(float(items_count) / shipping_option.postagePackSize)
                current_price = parcels_count * shipping_option.postageAmount + (items_count - parcels_count) * shipping_option.postageAmountAdd

            if min_price is None or current_price < min_price:
                min_price = current_price

        return min_price