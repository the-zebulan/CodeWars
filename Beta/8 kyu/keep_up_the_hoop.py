def hoopCount(n):
    """ hoop_count == PEP8, forced mixedCase by CodeWars """
    return 'Great, now move on to tricks' if n >= 10 else\
        'Keep at it until you get it'

assert hoopCount(3) == "Keep at it until you get it" 
assert hoopCount(11) == "Great, now move on to tricks"
