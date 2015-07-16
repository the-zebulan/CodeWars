def goto(level, button):
    if not isinstance(level, int) or not isinstance(button, str) \
            or level not in range(4) or button not in map(str, range(4)):
        return 0
    return int(button) - level

assert goto(2, '4') == 0
assert goto(4, '0') == 0
assert goto(3, None) == 0
assert goto(None, '2') == 0
assert goto([], '2') == 0
assert goto(3, {}) == 0
assert goto(2, '') == 0
assert goto(0, '2') == 2
assert goto(3, '1') == -2
assert goto(2, '2') == 0
