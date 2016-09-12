from collections import Counter


def buy_tofu(cost, box):
    cnt = Counter(a for a in box.split() if a in ('mon', 'monme'))
    total_mons = cnt['mon']
    total_monmes = cnt['monme']
    monme_value = total_monmes * 60
    max_mons = cost - monme_value
    quo, rem = divmod(cost, 60)
    if quo <= total_monmes and rem <= total_mons:
        coins = quo + rem
    elif total_mons >= max_mons:
        coins = total_monmes + max_mons
    else:
        return 'leaving the market'
    return [total_mons, total_monmes, total_mons + monme_value, coins]
