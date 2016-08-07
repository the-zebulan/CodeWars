def get_number_from_string(strng):
    return int(''.join(a for a in strng if a.isdigit()))
