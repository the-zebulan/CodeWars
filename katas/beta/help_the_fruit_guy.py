def remove_rotten(bag_of_fruits):
    return [] if not bag_of_fruits else \
        [fruit.replace('rotten', '').lower() for fruit in bag_of_fruits]
