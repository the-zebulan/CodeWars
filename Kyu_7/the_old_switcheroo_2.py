AZ = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6',
      'G': '7', 'H': '8', 'I': '9', 'J': '10', 'K': '11', 'L': '12',
      'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18',
      'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24',
      'Y': '25', 'Z': '26', 'a': '1', 'b': '2', 'c': '3', 'd': '4',
      'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
      'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16',
      'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22',
      'w': '23', 'x': '24', 'y': '25', 'z': '26'}


def encode(string):
    return ''.join(AZ.get(a, a) for a in string)

assert encode('abc') == '123'
assert encode('codewars') == '315452311819'
assert encode('abc-#@5') == '123-#@5'
assert encode('ABCD') == '1234'
assert encode('ZzzzZ') == '2626262626'
assert encode('this is a long string!! Please [encode] @C0RrEctly') == \
    '208919 919 1 1215147 1920189147!! 161251195 [51431545] @30181853201225'