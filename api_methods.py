from config import WEBAPI_KEY, COUNTRY_ID, ALLEGRO_LOGIN, ALLEGRO_PASSWORD

import hashlib

class ApiMethods:
    def __init__(self, client):
        self.client = client

    def get_items_list(self, options):
        return self.client.service.doGetItemsList(WEBAPI_KEY, COUNTRY_ID, options, resultScope = 3, resultSize = 1000).itemsList.item

    def get_version(self):
        status = self.client.service.doQueryAllSysStatus(COUNTRY_ID, WEBAPI_KEY)

        for sys in status.item:
            if sys.countryId == COUNTRY_ID:
                return sys.verKey

    def get_session(self, version):
        return self.client.service.doLoginEnc(ALLEGRO_LOGIN, hashlib.sha256(ALLEGRO_PASSWORD).digest().encode('base64'), COUNTRY_ID, WEBAPI_KEY, version).sessionHandlePart

    def get_items_info(self, session, item_ids):
        item_ids_struct = self.client.factory.create('ArrayOfLong')
        item_ids_struct.item = item_ids
        return self.client.service.doGetItemsInfo(session, item_ids_struct, getPostageOptions=1).arrayItemListInfo.item

    def get_shipment_data(self):
        print self.client.service.doGetShipmentData(COUNTRY_ID, WEBAPI_KEY)