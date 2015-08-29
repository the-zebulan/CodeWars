OUTPUT = '{}. {}\n'.format


def list_animals(animals):
    return ''.join(OUTPUT(i, a) for i, a in enumerate(animals, start=1))

    # result = ''
    # for i in xrange(len(animals)):
    #     result += str(i + 1) + '. ' + animals[i] + '\n'
    # return result

assert list_animals(['dog', 'cat', 'elephant']) == \
    '1. dog\n2. cat\n3. elephant\n'
