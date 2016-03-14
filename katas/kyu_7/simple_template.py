from re import compile, finditer

REGEX = compile(r'\{\{([a-zA-Z]+)\}\}')
REPLS = ('{{', '{'), ('}}', '}')


def create_template(s):
    def my_template(**kwargs):
        keys = {a.group(1): '' for a in finditer(REGEX, s)}
        keys.update(kwargs)
        return reduce(lambda a, kv: a.replace(*kv), REPLS, s).format(**keys)
    return my_template
