def remove_rotten(bag_of_fruits):
    return [] if not bag_of_fruits else \
        [fruit.replace('rotten', '').lower() for fruit in bag_of_fruits]


assert remove_rotten(['rottenApple', 'rottenBanana', 'rottenApple',
                    'rottenPineapple', 'rottenKiwi']) == \
    ['apple', 'banana', 'apple', 'pineapple', 'kiwi']
assert remove_rotten([]) == []
