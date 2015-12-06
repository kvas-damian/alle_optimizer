from config import WEBAPI_KEY, COUNTRY_ID, wsdl
from suds.client import Client

client = Client(wsdl)

val = client.factory.create("ArrayOfString")
val.item = "sdf"

option = client.factory.create("FilterOptionsType")
option.filterId = "search"
option.filterValueId = val

options = client.factory.create("ArrayOfFilteroptionstype")
options.item = option

alleRes = client.service.doGetItemsList(WEBAPI_KEY, COUNTRY_ID, options, resultScope = 0, resultSize = 1000)

print alleRes
