def shorten(strng, length, glue='...'):
    glue_length = len(glue)
    without_glue_length = length - glue_length
    if len(strng) <= length:
        return strng
    elif without_glue_length < 2:
        return strng[:length]
    quo, rem = divmod(without_glue_length, 2)
    return '{}{}{}'.format(strng[:quo], glue, strng[-(quo + rem):])
