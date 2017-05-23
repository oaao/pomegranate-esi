import seeds

# example functionality as development continues


# A. ORDERS: retrieve orders data as often as possible
# -- single case example: market orders in Rens
rens_grouped    = seeds.orders_distill('Rens', 10)
rens_ungrouped  = [x for page in rens_grouped for order in page.values() for x in order]
print('Rens currently has {} traded typeIDs with a total of {} market orders.'
      .format(len(rens_grouped), len(rens_ungrouped)))

# B. TYPE IDs: we eventually want a persistent list of all item types traded in the five main hubs to pass to HISTORY
# -- single case, non-persistent example: traded type IDs in Rens
rens_type_ids = [x for order_set in rens_grouped for x in order_set.keys()]

# -- truncate this for example purposes, since we need to rate-limit type ID requests
example_ids = rens_type_ids[:100]

# C. HISTORY: we eventually want a daily lookup of the previous day's market history for a given type ID
# -- single case, non-persistent example: market history in Rens for currently traded items in Rens
rens_history = seeds.history_distill('Rens', example_ids)

