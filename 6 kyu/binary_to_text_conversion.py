def binary_to_string(binary):
    return ''.join(chr(int(binary[a:a + 8], 2))
                   for a in xrange(0, len(binary), 8))


assert binary_to_string('0100100001100101011011000110110001101111') == 'Hello'
assert binary_to_string('00110001001100000011000100110001') == '1011'
