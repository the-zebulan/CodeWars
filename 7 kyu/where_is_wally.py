from re import compile, search

REGEX = compile(r'(^|(?<= ))Wally(\W|$)')
# replaced my REGEX with one from @GiacomoSorbi on CodeWars, much cleaner


def wheres_wally(string):
    try:
        return search(REGEX, string).start()
    except AttributeError:
        return -1

assert wheres_wally('Walley ,Wally -Wally ;Wally +Wally :Wally') == -1
assert wheres_wally('Walley Wally, Wally- Wally: Wally+ Wally:') == 7
assert wheres_wally('.Wally') == -1
assert wheres_wally('') == -1
assert wheres_wally('WAlly') == -1
assert wheres_wally('wAlly') == -1
assert wheres_wally('Wally') == 0
assert wheres_wally('Where\'s Wally') == 8
assert wheres_wally('Wallyd') == -1
assert wheres_wally('It\'s Wally\'s.') == 5
