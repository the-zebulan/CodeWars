from re import compile, search

REGEX = compile(r'(^|(?<= ))Wally(\W|$)')
# replaced my REGEX with one from @GiacomoSorbi on CodeWars, much cleaner


def wheres_wally(string):
    try:
        return search(REGEX, string).start()
    except AttributeError:
        return -1
