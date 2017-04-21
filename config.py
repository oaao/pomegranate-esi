# static configurations


def get_station(hub_name):
    hubs = {
        'jita':    {'region_id': '10000002', 'system_id': '30000142', 'station_id': '60003760'},
        'amarr':   {'region_id': '10000043', 'system_id': '30002187', 'station_id': '60008494'},
        'dodixie': {'region_id': '10000032', 'system_id': '30002659', 'station_id': '60011866'},
        'hek':     {'region_id': '10000042', 'system_id': '30002053', 'station_id': '60005686'},
        'rens':    {'region_id': '10000030', 'system_id': '30002510', 'station_id': '60004588'}
    }
    hub_id = hubs[hub_name.lower()]
    return hub_id
