def cycle(arg, all_ids=None):
    if all_ids is None:
        all_ids = set()
    arg_id = id(arg)
    if arg_id not in all_ids:
        all_ids.add(arg_id)
        if isinstance(arg, list):
            for a in arg:
                for b in cycle(a, all_ids):
                    yield b
        elif isinstance(arg, dict):
            for k, v in sorted(arg.iteritems()):
                for c in cycle(v, all_ids):
                    yield c
        else:
            yield arg
