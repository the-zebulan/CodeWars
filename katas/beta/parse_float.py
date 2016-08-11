def parse_float(strng):
    try:
        return float(strng)
    except (TypeError, ValueError):
        return None
