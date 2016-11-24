from textwrap import TextWrapper


def align_right(text, width):
    tw = TextWrapper(width, break_on_hyphens=False)
    return '\n'.join(a.rjust(width) for a in tw.wrap(text))
