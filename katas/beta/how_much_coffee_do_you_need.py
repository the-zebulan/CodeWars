def how_much_coffee(lst):
    result = sum(a.isalpha() if a.islower() else 2 * a.isalpha() for a in lst)
    return 'You need extra sleep' if result > 3 else result
