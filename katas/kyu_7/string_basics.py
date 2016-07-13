def get_users_ids(strng):
    return [a.replace('uid', '', 1).strip()
            for a in strng.lower().replace('#', '').split(',')]
