def lineup_students(names):
    return sorted(names.split(), key=lambda a: (len(a), a), reverse=True)
