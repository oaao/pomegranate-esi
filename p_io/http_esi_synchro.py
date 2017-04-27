# a 'dumb' temporary synchronous HTTP placeholder, to be ultimately replaced with async functionality

import config
import modifiers

import requests

# consider using an inheritance model for orders/citadel/history esp. since their data will be used differently anyhow


class EsiMarketClient:

    ESI_URL = 'https://esi.tech.ccp.is/latest/'

    ESI_ENDPTS = {
        'orders':   'markets/{}/orders/',
        'history':  'markets/{}/history/',
        'citadels': 'markets/structures/{}/'
    }

    def __init__(self, hub_name):
        hub_data = config.get_hub(hub_name.lower())

        self.hub        = hub_name.lower()
        self.region_id  = hub_data['region_id']
        # self.system_id  = hub_data['system_id']
        # self.station_id = hub_data['station_id']

        self.orders   = []
        self.history  = []
        # self.citadels = []    # class not currently structured with citadel endpoint in mind

    def _url_format(self, req_type, num_id):
        return self.ESI_URL + self.ESI_ENDPTS[req_type].format(num_id)

    # fully abstracted retrieval once differences between orders, history, citadels are properly understood
    # currently only supports one parameter per call
    def _retrieve(self, req_type, params):
        url        = self._url_format(req_type, str(self.region_id))
        param_name, param_values = params

        # retries  = []
        # failures = {}

        data     = []

        with requests.Session() as s:
            for param_val in param_values:
                param = {param_name: param_val}
                print('\nTrying: {} with param {}'.format(url, param))
                resp = s.get(url, params=param)
                print('Status {} ---- {} results.'.format(resp.status_code, len(resp.json())))
                if resp.status_code == 200 and resp.json():    # placeholder validation
                    data.append({param_val: resp.json()})

        return data

    @modifiers.timed
    def get_orders(self, pages):
        params      = ('page', range(1, pages+1))

        unflattened = self._retrieve('orders', params)
        self.orders = [x for page in unflattened for order in list(page.values()) for x in order]
        print('\nGot {} market orders.'.format(len(self.orders)))

    @modifiers.timed
    def get_history(self, type_ids):
        params       = ('type_id', type_ids)

        self.history = self._retrieve('history', params)
        print('\nGot {} market history elements for {} given type IDs.'.format(len(self.history), len(type_ids)))

    def get_citadels(self):
        # not currently accounted for
        pass
