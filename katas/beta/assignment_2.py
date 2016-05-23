from string import ascii_lowercase, maketrans


def mirror(code, rev=ascii_lowercase):  # python 2
    half = len(rev) // 2
    the_mirror = (rev[:half][::-1] + rev[::-1][:half]).lower()
    return code.lower().translate(maketrans(the_mirror, the_mirror[::-1]))


# from string import ascii_lowercase
#
#
# def mirror(code, rev=ascii_lowercase):  # python 3
#     half = len(rev) // 2
#     the_mirror = (rev[:half][::-1] + rev[::-1][:half]).lower()
#     return code.lower().translate(str.maketrans(the_mirror, the_mirror[::-1]))
