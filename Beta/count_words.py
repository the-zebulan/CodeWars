from re import compile, finditer

OMIT = {'a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as'}
REGEX = compile(r'[a-z]+')


def word_count(s):
    return sum(a.group() not in OMIT for a in finditer(REGEX, s.lower()))


assert word_count('Hello there, little user5453 374 ())$.') == 4
assert word_count("hello there") == 2
assert word_count("hello there and hi") == 4
assert word_count("Really2374239847 long ^&#$&(*@# sequence") == 3
assert word_count(
    "I'd been using my sphere as a stool. I traced counterclockwise"
    " circles on it with my fingertips and it shrank until I could "
    "palm it. My bolt had shifted while I'd been sitting. I pulled "
    "it up and yanked the pleats straight as I careered around "
    "tables, chairs, globes, and slow-moving fraas. I passed under "
    "a stone arch into the Scriptorium. The place smelled richly of"
    " ink. Maybe it was because an ancient fraa and his two fids "
    "were copying out books there. But I wondered how long it would"
    " take to stop smelling that way if no one ever used it at all;"
    " a lot of ink had been spent there, and the wet smell of it "
    "must be deep into everything.") == 112
