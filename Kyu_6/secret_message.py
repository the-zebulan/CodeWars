def find_secret_message(paragraph):
    unique = set()
    result = []
    for word in (a.strip('.,:!?').lower() for a in paragraph.split()):
        if word in unique and word not in result:
            result.append(word)
        unique.add(word)
    return ' '.join(result)
