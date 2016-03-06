def search_names(logins):
    return filter(lambda (a, _): a.endswith('_'), logins)
