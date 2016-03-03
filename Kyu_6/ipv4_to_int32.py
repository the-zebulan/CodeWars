BINARY = '{0:08b}'.format


def ip_to_int32(ip):
    return int(''.join(BINARY(int(a)) for a in ip.split('.')), 2)

assert ip_to_int32("128.114.17.104") == 2154959208
assert ip_to_int32("0.0.0.0") == 0
assert ip_to_int32("128.32.10.1") == 2149583361
