from collections import defaultdict


def recoverSecret(triplets):
    letters = defaultdict(set)
    for a, b, c in triplets:
        letters[a].add(b)
        letters[a].add(c)
        letters[b].add(c)

    for key, value in letters.items():
        for after_key in value:
            letters[key] = letters[key].union(letters[after_key])

    return ''.join(k for k, _ in sorted(
        letters.iteritems(), key=lambda (_, v): len(v), reverse=True
    ))
