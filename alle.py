# -*- coding: utf-8 -*-

from config import wsdl
from item import Item
from url_parser import UrlParser
from alle_options import AlleOptions
from api_methods import ApiMethods
from suds.client import Client

shipment_options = {
    1: "Paczka pocztowa ekonomiczna",
    2: "List ekonomiczny",
    3: "Paczka pocztowa priorytetowa",
    4: "List priorytetowy",
    5: "Przesyłka pobraniowa / Paczka48 pobranie",
    6: "List polecony ekonomiczny",
    7: "Przesyłka pobraniowa priorytetowa / Paczka24 pobranie",
    8: "List polecony priorytetowy",
    9: "Przesyłka kurierska",
    10: "Odbiór osobisty",
    11: "Przesyłka kurierska pobraniowa",
    12: "Przesyłka elektroniczna (e-mail)",
    13: "Odbiór osobisty po przedpłacie",
    16: "Allegro Polecony InPost",
    17: "Allegro Kurier InPost",
    18: "Allegro Kurier InPost (za pobraniem)",
    21: "Pocztex Kurier48",
    22: "Pocztex Kurier48 pobraniowy",
    30: "Paczka24",
    31: "Paczka48",
    10006: "Odbiór w punkcie po przedpłacie - PACZKA W RUCHu",
    10022: "Odbiór w punkcie po przedpłacie - Paczkomaty 24/7",
    10023: "Odbiór w punkcie po przedpłacie - Allegro Paczkomaty InPost",
    10060: "Odbiór w punkcie po przedpłacie - Paczka24 Odbiór w Punkcie",
    10061: "Odbiór w punkcie po przedpłacie - E-PRZESYŁKA / Paczka48 Odbiór w Punkcie",
    20006: "Odbiór w punkcie - PACZKA W RUCHu",
    20022: "Odbiór w punkcie - Paczkomaty 24/7",
    20023: "Odbiór w punkcie - Allegro Paczkomaty InPost",
    20060: "Odbiór w punkcie - Paczka24 Odbiór w Punkcie",
    20061: "Odbiór w punkcie - E-PRZESYŁKA / Paczka48 Odbiór w Punkcie"
}

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

items = api_methods.get_items_list(options)

item_ids = [x.itemId for x in items]

for i in xrange(0, len(item_ids), 25):
    current_item_ids = item_ids[i:i+25]
    items_info = api_methods.get_items_info(session, current_item_ids)

    for item_info in items_info:
        print item_info.itemInfo.itId, item_info.itemInfo.itName, item_info.itemInfo.itBuyNowPrice
        item = Item(item_info.itemInfo.itId, item_info.itemInfo.itName, item_info.itemInfo.itBuyNowPrice)

        item.add_shiping_options([x for x in item_info.itemPostageOptions.item])
        print item.get_lowest_shipping_price(3)