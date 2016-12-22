short = lambda arr: __import__('collections').Counter(__import__('itertools').chain.from_iterable(arr))
