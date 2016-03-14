def ghostbusters(building):
    return building.replace(' ', '') if building.find(' ') > -1 \
        else 'You just wanted my autograph didn\'t you?'
