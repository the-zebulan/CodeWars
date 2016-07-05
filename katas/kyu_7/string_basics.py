def get_users_ids(strng):
    result = []
    for a in strng.split(','):
        result.append(a.lower().replace('#', '').replace('uid', '', 1).strip())
    return result
