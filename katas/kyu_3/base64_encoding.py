from base64 import b64encode, b64decode


def to_base_64(strng):
    return b64encode(strng).rstrip('=')


def from_base_64(strng):
    missing_padding = 4 - len(strng) % 4
    if missing_padding:
        strng += b'=' * missing_padding
    return b64decode(strng)
