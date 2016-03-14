def palindrome_chain_length(num):
    steps = 0
    while True:
        tmp = str(num)
        rev = tmp[::-1]
        if tmp == rev:
            return steps
        num += int(rev)
        steps += 1
