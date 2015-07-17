def search_names(logins):
    return filter(lambda (a, _): a.endswith('_'), logins)

assert search_names([["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]) == \
    [["bar_", "bar@bar.com"]]
