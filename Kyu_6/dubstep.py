def song_decoder(song):
    return ' '.join(a for a in song.split('WUB') if a)

assert song_decoder('AWUBBWUBC') == 'A B C'
assert song_decoder('AWUBWUBWUBBWUBWUBWUBC') == 'A B C'
assert song_decoder('WUBAWUBBWUBCWUB') == 'A B C'
