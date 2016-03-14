def hashify(string):
    result = {}
    string = string + string[0]
    for a in xrange(len(string) - 1):
        k, v = string[a:a + 2]
        try:
            result[k].append(v)         # dictionary value is a list
        except AttributeError:
            result[k] = [result[k], v]  # dictionary value is NOT a list
        except KeyError:
            result[k] = v               # dictionary key does NOT exist
    return result
