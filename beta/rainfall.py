from collections import defaultdict


def data_to_dict(data, get_mean=True):
    result = defaultdict(dict)
    for place in data.split('\n'):
        all_temps = []
        key, temps = place.split(':')
        temps_sum = total_temps = 0.0
        for temp in temps.split(','):
            t = float(temp.split()[1])
            temps_sum += t
            total_temps += 1
            all_temps.append(t)
        temps_mean = temps_sum / total_temps
        result[key]['mean'] = temps_mean
        if get_mean:
            continue

        total = 0.0
        for temp in all_temps:
            total += (temp - temps_mean) ** 2
        result[key]['variance'] = total / total_temps
    return result


def mean(town, strng):
    try:
        return data_to_dict(strng)[town]['mean']
    except KeyError:
        return -1


def variance(town, strng):
    try:
        return data_to_dict(strng, False)[town]['variance']
    except KeyError:
        return -1
