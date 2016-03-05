def binary_to_string(binary):
    return ''.join(chr(int(binary[a:a + 8], 2))
                   for a in xrange(0, len(binary), 8))
