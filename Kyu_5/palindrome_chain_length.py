def palindrome_chain_length(num):
    steps = 0
    while True:
        tmp = str(num)
        rev = tmp[::-1]
        if tmp == rev:
            return steps
        num += int(rev)
        steps += 1


assert palindrome_chain_length(87) == 4
assert palindrome_chain_length(1) == 0
assert palindrome_chain_length(88) == 0
assert palindrome_chain_length(89) == 24
assert palindrome_chain_length(10) == 1
