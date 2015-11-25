def find(item, items):
    return item in items


assert find('hello', ['bye bye', 'hello']) is True
assert find('anything', ['bye bye', 'hello']) is False
