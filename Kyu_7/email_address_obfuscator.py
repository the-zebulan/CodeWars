REPLACEMENTS = ('.', ' [dot] '), ('@', ' [at] ')


def obfuscate(email):
    return reduce(lambda a, kv: a.replace(*kv), REPLACEMENTS, email)
