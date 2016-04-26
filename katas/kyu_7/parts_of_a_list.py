def partlist(arr):
    return [(' '.join(arr[:a]), ' '.join(arr[a:]))
            for a in xrange(1, len(arr))]
