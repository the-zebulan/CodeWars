def separate_filename_from_extension(s):
    slash = s.rfind('/') + 1
    dex = slash + s[slash:].find('.', s[slash:].startswith('.'))
    return s[:dex], s[dex:]
