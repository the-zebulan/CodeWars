def archers_ready(archers):
    return all(a >= 5 for a in archers) if archers else False
