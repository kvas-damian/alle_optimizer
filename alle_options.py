
class AlleOptions:

    def __init__(self, client):
        self.client = client

    def get_options(self, params):
        options = self.client.factory.create("ArrayOfFilteroptionstype")

        for param_name, param_value in params.items():
            # TODO
            if param_name == 'state':
                continue

            option = self.client.factory.create("FilterOptionsType")
            option.filterId = param_name

            if isinstance(param_value, dict):
                val = self.client.factory.create("RangeValueType")
                if 'min' in param_value:
                    val.rangeValueMin = param_value['min']
                if 'max' in param_value:
                    val.rangeValueMax = param_value['max']

                option.filterValueRange = val
            else:
                val = self.client.factory.create("ArrayOfString")
                val.item = param_value

                option.filterValueId = val

            options.item.append(option)

        return options
