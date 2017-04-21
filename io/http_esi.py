# Handle all HTTP / ESI API work:
# input validation, correctly navigating ESI endpoints, rate limiting, async retrieval

# currently a bunch of spaghetti

import curio
import asks

ESI_URL = 'https://esi.tech.ccp.is/latest/'

ESI_ENDPTS = {
    'orders': 'markets/{}/orders/',
    'history': 'markets/{}/history/',
    'citadels': 'markets/structures/{}/'
}

data = []


async def session_gen(req_type, num_id):
    s_config = asks.HSession(ESI_URL,
                             endpoint=ESI_ENDPTS[req_type].format(num_id),
                             connections=5)
    return s_config


async def retrieve(page, req_type, num_id):
    s = session_gen(req_type, num_id)
    r = await s.get(params={'page': str(page)})
    # replace this with resp code
    if r.json():
        return r


async def spawner(req_type, num_id):
    count = 1
    stop = False
    while not stop:
        async with curio.TaskGroup() as grp:
            for i in range(1):
                print('\nSpawning {}:'.format(i))
                print('data', len(data))
                await grp.spawn(retrieve(count, req_type, num_id))
                await curio.sleep(1)
                count += 1
            async for task in grp:
                if task.result:
                    data.append(task.result)
                else:
                    stop = True

# curio.run(spawner(req_type='orders', num_id=10000002))
