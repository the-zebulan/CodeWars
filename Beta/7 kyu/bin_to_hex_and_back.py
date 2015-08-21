TO_BIN = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
          'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
TO_HEX = {v: k for k, v in TO_BIN.iteritems()}


def hex_to_bin(hex_string):
    return ''.join(TO_BIN[a] for a in hex_string.lower()).lstrip('0') or '0'
    # return '{:b}'.format(int(hex_string, 16))


def bin_to_hex(binary_string):
    length = len(binary_string)
    q, r = divmod(length, 4)
    if r > 0:
        length = 4 * (q + 1)
        binary_string = binary_string.zfill(length)
    return ''.join(TO_HEX[binary_string[a:a + 4]]
                   for a in range(0, length, 4)).lstrip('0') or '0'
    # return '{:x}'.format(int(binary_string, 2))

assert bin_to_hex('000101') == '5'
assert bin_to_hex('001111') == 'f'
assert bin_to_hex('000') == '0'
assert bin_to_hex('10011010010') == '4d2'

assert hex_to_bin('0') == '0'
assert hex_to_bin('f') == '1111'
assert hex_to_bin('0F') == '1111'
assert hex_to_bin('5') == '101'
assert hex_to_bin('04D2') == '10011010010'
assert hex_to_bin('A23') == '101000100011'
