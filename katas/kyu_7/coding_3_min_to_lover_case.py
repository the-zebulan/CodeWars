from string import ascii_uppercase

AZ = {k: i for i, k in enumerate(ascii_uppercase)}


def to_lover_case(strng):
    love = 'LOVE'
    result = []
    for a in strng.upper():
        dex = AZ.get(a)
        result.append(a if dex is None else love[dex % 4])
    return ''.join(result)
