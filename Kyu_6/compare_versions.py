from itertools import izip_longest


def compare_versions(version1, version2):
    if version1 == version2:
        return True
    for v1, v2 in izip_longest((int(a) for a in version1.split('.')),
                               (int(b) for b in version2.split('.')),
                               fillvalue=0):
        if v1 > v2:
            return True
        elif v1 < v2:
            return False
