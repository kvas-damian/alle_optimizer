import unittest
import sys

sys.path.append('..')
from url_parser import UrlParser


class UrlParserTestCase(unittest.TestCase):
    def test_parse(self):
        url_parser = UrlParser()
        url = "http://allegro.pl/listing/listing.php?order=d&string=asd&bmatch=engagement-v6-promo-sm-sqm-dyn-v2-aut-1-1-1120&buyNew=1&offerTypeBuyNow=1&price_from=1&price_to=2&city=test&startingTime=6&state=9&standard_allegro=1&freeReturn=1&freeShipping=1&personal_rec=1&vat_invoice=1&generalDelivery_rec=1"
        self.assertEqual(url_parser.parse(url), {'search': 'asd', 'offerType': ['buyNow'], 'condition': ['new'], 'price': {'min': '1', 'max': '2'}, 'city': 'test', 'state': '9', 'startingTime': '12h', 'offerOptions': ['freeReturn', 'freeShipping', 'personalReceipt', 'vatInvoice', 'generalDelivery', 'standardAllegro']})


if __name__ == '__main__':
    unittest.main()