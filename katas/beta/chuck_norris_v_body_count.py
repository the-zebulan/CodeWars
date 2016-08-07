from re import search


def body_count(code):
    return bool(search(r'(?:[A-Z]\d){5}\.-[A-Z]%\d\.\d{2}\.', code))
