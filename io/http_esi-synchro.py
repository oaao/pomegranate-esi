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

    def __init__(self, hub):
        hub_data = config.get_station(hub)

        self.hub        = hub
        self.region_id  = hub_data['region_id']
        # self.system_id  = hub_data['system_id']
        # self.station_id = hub_data['station_id']

        self.orders   = []
        # self.history  = []    # class not currently structured with market history in mind
        # self.citadels = []    # class not currently structured with market history in mind

    def _url_format(self, req_type, num_id):
        return self.ESI_URL + self.ESI_ENDPTS[req_type].format(num_id)

    # fully abstracted retrieval once differences between orders, history, citadels are properly understood
    def _retrieve(self, url_list):

        # retries  = []
        # failures = {}

        data     = []

        with requests.Session() as s:
            for url in url_list:
                print('\nTrying: {}'.format(url))
                resp = s.get(url)
                print('Status {} ---- {} results.'.format(resp.status_code, len(resp.json())))
                if resp.status_code == 200 and resp.json():    # placeholder validation
                    data += resp.json()
        return data

    @modifiers.timed
    def get_orders(self, pages):
        print('\nGetting market orders for {}:'.format(self.hub))
        url        = self._url_format('orders', self.region_id) + '?page={}'
        order_urls = [url.format(x) for x in range(1, pages+1)]

        self.orders = self._retrieve(order_urls)
        print('\nGot {} market orders.'.format(len(self.orders)))

    def get_history(self):
        # not currently accounted for
        pass

    def get_citadels(self):
        # not currently accounted for
        pass


# rens = EsiMarketClient('rens')
# rens.get_orders(pages=10)

