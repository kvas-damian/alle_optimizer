from math import ceil

class Item(object):
    personal_receipt_ids = [10, 13]
    not_registered_ids = [2, 4]

    def __init__(self, item_info, shipping_options):
        self.item_info = item_info
        self.shipping_options = shipping_options

    def get(self, attr_name):
        return getattr(self.item_info, 'it' + attr_name[0].upper() + attr_name[1:])

    def get_url(self):
        return 'http://allegro.pl/ShowItem2.php?item=%d' % self.get('id')

    def get_lowest_shipping_price(self, items_count, skip_not_registered=False):
        if self.get('quantity') < items_count:
            return None

        min_price = None

        for shipping_option in self.shipping_options:
            if shipping_option.postageId in self.personal_receipt_ids or (skip_not_registered and shipping_option.postageId in self.not_registered_ids):
                # don't include personal receipts and not registered
                continue

            if shipping_option.postageFreeShipping:
                current_price = 0
            else:
                parcels_count = ceil(float(items_count) / shipping_option.postagePackSize)
                current_price = parcels_count * shipping_option.postageAmount + (items_count - parcels_count) * shipping_option.postageAmountAdd

            if min_price is None or current_price < min_price:
                min_price = current_price

        return min_price