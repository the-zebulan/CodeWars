def shorten(string, length, glue='...'):
    glue_length = len(glue)
    without_glue_length = length - glue_length
    if len(string) <= length:
        return string
    elif without_glue_length < 2:
        return string[:length]
    quo, rem = divmod(without_glue_length, 2)
    return '{}{}{}'.format(string[:quo], glue, string[-(quo + rem):])
