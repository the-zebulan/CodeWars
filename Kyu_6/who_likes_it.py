def likes(names):
    length = len(names)
    if length < 2:
        return '{} likes this'.format('no one' if not length else names[0])
    elif length < 4:
        return '{} and {} like this'.format(', '.join(names[:-1]), names[-1])
    return '{} and {} others like this'.format(', '.join(names[:2]), length - 2)


assert likes([]) == "no one likes this"
assert likes(["Peter"]) == "Peter likes this"
assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
assert likes(["Alex", "Jacob", "Mark", "Max"]) \
    == "Alex, Jacob and 2 others like this"
