from string import ascii_lowercase

AZ = ' ' + ascii_lowercase


def decrypt(msg):
    return ''.join(
        AZ[sum(int(b) for b in a if b.isdigit()) % 27] for a in msg.split())
