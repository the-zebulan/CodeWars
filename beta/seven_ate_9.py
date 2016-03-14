from re import sub


def seven_ate9(string):
    return sub('(?<=7)9+(?=7)', '', string)
