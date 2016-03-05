BINARY = '{0:08b}'.format


def ip_to_int32(ip):
    return int(''.join(BINARY(int(a)) for a in ip.split('.')), 2)
