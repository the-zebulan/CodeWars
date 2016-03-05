def song_decoder(song):
    return ' '.join(a for a in song.split('WUB') if a)
