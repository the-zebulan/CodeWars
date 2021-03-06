TO_UPC = {'0011001': '1', '1000010': '3', '0111101': '3', '1110010': '0',
          '0001101': '0', '0100011': '4', '1000100': '7', '0101111': '6',
          '1001000': '8', '0111011': '7', '1011100': '4', '0001011': '9',
          '1101100': '2', '1001110': '5', '0110001': '5', '0010011': '2',
          '1110100': '9', '1100110': '1', '0110111': '8', '1010000': '6'}


def barcode_scanner(barcode):
    l_r = barcode[3:45] + barcode[50:-3]
    return ''.join(TO_UPC[l_r[a:a + 7]] for a in xrange(0, 84, 7))


# # This kata on CodeWars forces the 'digits' dictionary...
# # 'digits' should be hidden, not in every solution!
# digits = {'S': '1B1W1B', 'E': '1B1W1B', 'M': '1W1B1W1B1W', '0': '3W2B1W1B',
#           '1': '2W2B2W1B', '2': '2W1B2W2B', '3': '1W4B1W1B', '4': '1W1B3W2B',
#           '5': '1W2B3W1B', '6': '1W1B1W4B', '7': '1W3B1W2B', '8': '1W2B1W3B',
#           '9': '3W1B1W2B'}
