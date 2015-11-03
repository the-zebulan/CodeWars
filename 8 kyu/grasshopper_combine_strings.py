def combine_names(*args):
    return ' '.join(args)

assert combine_names("James", "Stevens") == "James Stevens"
assert combine_names("Davy", "Back") == "Davy Back"
assert combine_names("Arthur", "Dent") == "Arthur Dent"
