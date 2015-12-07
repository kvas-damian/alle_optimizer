from config import wsdl
from url_parser import UrlParser
from alle_options import AlleOptions
from api_methods import ApiMethods
from suds.client import Client

client = Client(wsdl)
url = "http://allegro.pl/listing/listing.php?order=d&string=samsung&bmatch=engagement-v6-promo-sm-sqm-ele-1-1-1130&buyNew=1&offerTypeBuyNow=1&price_to=1000&city=Warszawa&vat_invoice=1&generalDelivery_rec=1&standard_allegro=1&startingTime=7"
url_parser = UrlParser()
params = url_parser.parse(url)

alle_options_parser = AlleOptions(client)
options = alle_options_parser.get_options(params)

# TODO city UTF
print options

api_methods = ApiMethods(client)

api_version = api_methods.get_version()
session = api_methods.get_session(api_version)

# items = api_methods.get_items_list(options)
#
# for item in items:
#     print item.itemId, item.itemTitle


