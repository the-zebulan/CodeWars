from string import ascii_lowercase

AZ = set(ascii_lowercase)


def is_pangram(string):
    """ Thanks to 'hiasen' on CodeWars for the idea of using subset """
    return AZ.issubset(set(string.lower()))
    # return set(a for a in string.lower() if a.isalpha()) == AZ
