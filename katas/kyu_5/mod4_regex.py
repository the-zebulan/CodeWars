import re


class Mod:
    mod4 = re.compile(r'.*\[[+-]?0*(\d*[13579][26]|(?:\d*[02468])?[048])\]')
