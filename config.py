# static configurations


def get_hub(hub_name):

    hub_key = ['region_id', 'system_id', 'station_id']
    hub_ids = {
        'jita':    ('10000002', '30000142', '60003760'),
        'amarr':   ('10000043', '30002187', '60008494'),
        'dodixie': ('10000032', '30002659', '60011866'),
        'hek':     ('10000042', '30002053', '60005686'),
        'rens':    ('10000030', '30002510', '60004588')
    }

    if hub_name in hub_ids:
        hub_data = {k: v for k, v in zip(hub_key, hub_ids[hub_name.lower()])}

        return hub_data
