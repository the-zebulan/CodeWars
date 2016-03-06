def goto(level, button):
    if not isinstance(level, int) or not isinstance(button, str) \
            or level not in xrange(4) or button not in map(str, xrange(4)):
        return 0
    return int(button) - level
