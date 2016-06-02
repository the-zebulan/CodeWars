def is_audio(filename):
    name, ext = filename.split('.')
    return name.isalpha() and ext in {'mp3', 'flac', 'alac', 'aac'}


def is_img(filename):
    name, ext = filename.split('.')
    return name.isalpha() and ext in {'jpg', 'jpeg', 'png', 'bmp', 'gif'}
