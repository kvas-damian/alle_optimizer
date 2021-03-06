import urlparse

class UrlParser:
    def __init__(self):
        pass

    def parse(self, url):
        parsed_params = {}
        params = urlparse.parse_qs(url)

        parsed_params.update(self._get_category(params, urlparse.urlparse(url).path))
        parsed_params.update(self._get_search(params))
        parsed_params.update(self._get_offer_type(params))
        parsed_params.update(self._get_price(params))
        parsed_params.update(self._get_condition(params))
        parsed_params.update(self._get_starting_time(params))
        parsed_params.update(self._get_offer_options(params))

        simple_params = ['city', 'state']
        for simple_param in simple_params:
            parsed_params.update(self._get_simple(params, simple_param))
        return parsed_params

#TODO finish category
    def _get_category(self, params, path):
        out = {}
        path_parts = path.split('-')
        if 'id' in params:
            out['category'] = params['id'][0]
        elif len(path_parts) > 1:
            out['category'] = path_parts[-1]

        return out

    def _get_search(self, params):
        out = {}
        if 'string' in params:
            out['search'] = params['string'][0].decode('UTF-8')
        return out

    def _get_offer_type(self, params):
        out = {}
        if 'offerTypeBuyNow' in params or 'offerTypeAuction' in params:
            out['offerType'] = []
        if 'offerTypeBuyNow' in params:
            out['offerType'].append('buyNow')
        if 'offerTypeAuction' in params:
            out['offerType'].append('auction')
        return out

    def _get_simple(self, params, param_name):
        out = {}
        if param_name in params:
                out[param_name] = params[param_name][0].decode('UTF-8')
        return out

    def _get_price(self, params):
        out = {}
        if 'price_from' in params or 'price_to' in params:
            out['price'] = {}
            if 'price_from' in params:
                out['price']['min'] = params['price_from'][0]
            if 'price_to' in params:
                out['price']['max'] = params['price_to'][0]

        return out

    def _get_condition(self, params):
        out = {}
        if 'buyNew' in params or 'buyUsed' in params:
            out['condition'] = []
        if 'buyNew' in params:
            out['condition'].append('new')
        if 'buyUsed' in params:
            out['condition'].append('used')
        return out

    def _get_offer_options(self, params):
        out = {}
        options = []
        if 'freeReturn' in params:
            options.append('freeReturn')
        if 'freeShipping' in params:
            options.append('freeShipping')
        if 'personal_rec' in params:
            options.append('personalReceipt')
        if 'vat_invoice' in params:
            options.append('vatInvoice')
        if 'generalDelivery_rec' in params:
            options.append('generalDelivery')
        if 'standard_allegro' in params:
            options.append('standardAllegro')

        if len(options):
            out['offerOptions'] = options

        return out

    def _get_starting_time(self, params):
        out = {}
        starting_times = {
            '1': '1h',
            '2': '2h',
            '3': '3h',
            '4': '4h',
            '5': '5h',
            '6': '12h',
            '7': '24h',
            '8': '2d',
            '9': '3d',
            '10': '4d',
            '11': '5d',
            '12': '6d',
            '13': '7d',
        }

        if 'startingTime' in params:
            out['startingTime'] = starting_times[params['startingTime'][0]]
        return out
