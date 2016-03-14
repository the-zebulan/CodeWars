from string import ascii_uppercase as az, maketrans


def caeser(message, key):
    return message.upper().translate(maketrans(az[-key:] + az[:-key], az))
