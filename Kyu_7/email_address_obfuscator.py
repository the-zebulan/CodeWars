REPLACEMENTS = ('.', ' [dot] '), ('@', ' [at] ')


def obfuscate(email):
    return reduce(lambda a, kv: a.replace(*kv), REPLACEMENTS, email)

assert obfuscate('test@123.com') == 'test [at] 123 [dot] com'
assert obfuscate('Code_warrior@foo.ac.uk') == 'Code_warrior [at] foo [dot] ac [dot] uk'
