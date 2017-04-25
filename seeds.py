# obtain, filter/organise, and store raw data

# using config, io_http, and io_db, write orderbooks and market histories to database

# main will govern this such that:
# - orderbooks are pulled as frequently as possible
# - market histories are pulled once per day per region/hub

from p_io import http_esi_synchro

import config
import arrow
from operator import itemgetter
from itertools import groupby


def market_import(hub_name, pages):
    importer = http_esi_synchro.EsiMarketClient(hub_name)
    importer.get_orders(pages)
    return importer.orders


def market_distill(hub_name, pages):
    data_raw = market_import(hub_name.lower(), pages)

    # filter out all NPC-station regional orders that are not in the hub's station
    # sloppily accounts for citadel orders - does not currently restrict by range to hub
    hub_station = config.get_hub(hub_name)['station_id']

    data_npc = [x for x in data_raw if x['location_id'] == hub_station]
    data_cit = [x for x in data_raw if x['location_id'] >= 1020000000000]
    data_hub = data_npc + data_cit

    print('\n{} hub orders filtered from {} regional orders.\n---- {} NPC station\n---- {} citadel'
          .format(len(data_hub), len(data_raw), len(data_npc), len(data_cit)))

    # replace datetime format with timestamp integers
    data_timestamp = data_hub
    for i in data_timestamp:
        i['issued'] = arrow.get(i['issued']).timestamp

    # group by typeID
    data_timestamp.sort(key=itemgetter('type_id'))
    data_grouped = [{k: list(v)} for k, v in groupby(data_timestamp, lambda x: x['type_id'])]

    # maybe: sub-group by buy vs. sell


def market_history():
    # gimme history
    pass


# market_distill('rens', 10)
