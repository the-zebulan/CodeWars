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


test = '''\
Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7'''

assert round(mean('London', test)) == 51.0
assert round(mean('Beijing', test)) == 52.0
assert round(variance('London', test)) == 57.0
assert round(variance('Beijing', test)) == 4808.0
