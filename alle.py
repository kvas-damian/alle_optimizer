from config import WEBAPI_KEY, COUNTRY_ID, wsdl
from url_parser import UrlParser
from alle_options import AlleOptions
from suds.client import Client

client = Client(wsdl)
url = "http://allegro.pl/listing/listing.php?order=d&string=samsung&bmatch=engagement-v6-promo-sm-sqm-ele-1-1-1130&buyNew=1&offerTypeBuyNow=1&price_to=1000&city=Warszawa&vat_invoice=1&generalDelivery_rec=1&standard_allegro=1&startingTime=7"
url_parser = UrlParser()
params = url_parser.parse(url)

alle_options_parser = AlleOptions(client)
options = alle_options_parser.get_options(params)

# TODO city UTF
print options
alleRes = client.service.doGetItemsList(WEBAPI_KEY, COUNTRY_ID, options, resultScope = 3, resultSize = 1000)

print alleRes


