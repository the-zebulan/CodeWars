def isAnagram(test, original):
    """ is_anagram == PEP8 (forced mixedCase by CodeWars) """
    return sorted(a for a in test.lower() if a.isalnum()) \
        == sorted(b for b in original.lower() if b.isalnum())


assert isAnagram("William Shakespeare", "I am a weakish speller") is True
assert isAnagram("Silent", "Listen") is True
assert isAnagram("Car", "Cat") is False
assert isAnagram("12345", "54321") is True
