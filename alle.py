from suds.client import Client

WEBAPI_KEY = "a776ff96"
COUNTRY_ID = 1

wsdl = "https://webapi.allegro.pl/service.php?wsdl"

client = Client(wsdl)

val = client.factory.create("ArrayOfString")
val.item = "sdf"

option = client.factory.create("FilterOptionsType")
option.filterId = "search"
option.filterValueId = val

options = client.factory.create("ArrayOfFilteroptionstype")
options.item = option

alleRes = client.service.doGetItemsList(WEBAPI_KEY, COUNTRY_ID, options, resultScope = 3, resultSize = 1000)

print alleRes
