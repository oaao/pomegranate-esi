import p_io.filesys
from seeds import orders_distill

type_ids = [t for x in orders_distill('jita', 40) for t in x.keys()]
print('\n{} unique typeIDs stored.'.format(len(type_ids)))

p_io.filesys.write_json(type_ids, 'type_ids')
