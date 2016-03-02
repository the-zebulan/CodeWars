def isAnagram(test, original):
    """ is_anagram == PEP8 (forced mixedCase by CodeWars) """
    return sorted(a for a in test.lower() if a.isalnum()) \
        == sorted(b for b in original.lower() if b.isalnum())
