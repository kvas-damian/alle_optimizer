from config import WEBAPI_KEY, COUNTRY_ID, wsdl
from url_parser import UrlParser
from alle_options import AlleOptions
from suds.client import Client

client = Client(wsdl)
url = "http://allegro.pl/listing/listing.php?personal_rec=1&generalDelivery_rec=1&state=15&vat_invoice=1&standard_allegro=1&freeShipping=1&startingTime=6&buyNew=1&offerTypeBuyNow=1&freeReturn=1&city=Wolsztyn&order=d&price_from=1&price_to=2&string=asd&bmatch=engagement-v6-promo-sm-sqm-dyn-v2-aut-1-1-1202"
url_parser = UrlParser()
params = url_parser.parse(url)

# TODO
params['search'] = 'samsung'

alle_options_parser = AlleOptions(client)
options = alle_options_parser.get_options(params)

# TODO city UTF
print options
alleRes = client.service.doGetItemsList(WEBAPI_KEY, COUNTRY_ID, options, resultScope = 0, resultSize = 1000)

# print alleRes


