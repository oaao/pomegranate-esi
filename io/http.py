# Handle all HTTP / ESI API work:
# input validation, correctly navigating ESI endpoints, rate limiting, async retrieval

# import aiohttp

ESI_URL = 'https://esi.tech.ccp.is/latest/markets/'

URL_OPTS = {
    'orders': '{}/orders/',
    'history': '{}/history/',
    'citadels': 'structures/{}/'
}


def url_define(num_id, req_type):
    return ESI_URL + URL_OPTS[req_type].format(num_id)