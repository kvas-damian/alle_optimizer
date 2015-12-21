import unittest
import sys
from unittest_data_provider import data_provider

sys.path.append('..')
from item import Item

class Object(object):
    pass

class ItemTestCase(unittest.TestCase):
    test_cases = lambda: (
        (7.5, 0.25, 5, 0, 1, 7.5,),
        (7.5, 0.25, 5, 0, 3, 8,),
        (7.5, 0.25, 5, 0, 6, 16,),
        (7.5, 0.25, 5, 0, 10, 17,),
        (7.5, 0.25, 5, 0, 13, 25,),
        (10, 1, 3, 0, 1, 10,),
        (10, 1, 3, 0, 5, 23,),
        (10, 1, 3, 1, 5, 0,),
        (25, 1, 3, 1, 6, 0,),
    )

    @data_provider(test_cases)
    def test_get_lowest_price(self, postage_price, ammout_add, package_size, free_shipping, items_count, expected):
        shipping_option = Object()
        shipping_option.postageId = 1
        shipping_option.postageAmount = postage_price
        shipping_option.postageAmountAdd = ammout_add
        shipping_option.postagePackSize = package_size
        shipping_option.postageFreeShipping = free_shipping
        item = Item(Object(), [shipping_option])
        self.assertAlmostEqual(item.get_lowest_shipping_price(items_count), expected)

if __name__ == '__main__':
    unittest.main()