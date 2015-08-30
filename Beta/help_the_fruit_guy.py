def removeRotten(bagOfFruits):
    # remove_rotten(bag_of_fruits) == PEP8, forced mixedCase by CodeWars
    return [] if not bagOfFruits else \
        [fruit.replace('rotten', '').lower() for fruit in bagOfFruits]

assert removeRotten(['rottenApple', 'rottenBanana', 'rottenApple',
                    'rottenPineapple', 'rottenKiwi']) == \
    ['apple', 'banana', 'apple', 'pineapple', 'kiwi']
assert removeRotten([]) == []
