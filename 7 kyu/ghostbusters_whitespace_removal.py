def ghostbusters(building):
    return building.replace(' ', '') if building.find(' ') > -1 \
        else 'You just wanted my autograph didn\'t you?'


assert ghostbusters('Factor y') == 'Factory'
assert ghostbusters('O  f fi ce') == 'Office'
assert ghostbusters('BusStation') == 'You just wanted my autograph didn\'t you?'
