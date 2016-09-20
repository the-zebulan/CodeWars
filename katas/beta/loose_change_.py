CHANGE = {'penny': 1, 'nickel': 5, 'dime': 10, 'quarter': 25, 'dollar': 100}


def change_count(change):
    return '${}.{:0>2}'.format(*divmod(
        sum(CHANGE[a] for a in change.split()), 100
    ))
