songs = [  # this list is hidden in CodeWars kata
    {'title': 'Keyleigh', 'playback': '03:36', 'artist': 'Marillion'},
    {'title': 'Time', 'playback': '06:48', 'artist': 'Pink Floyd'},
    {'title': 'YYZ', 'playback': '04:27', 'artist': 'Rush'},
    {'title': 'Days To Come', 'playback': '03:50', 'artist': 'Bonobo'},
    {'title': 'Yellow', 'playback': '04:32', 'artist': 'Coldplay'},
    {'title': 'Like Eating Glass', 'playback': '04:22',
     'artist': 'Bloc Party'},
    {'title': 'For Reasons Unknown', 'playback': '03:30',
     'artist': 'The Killers'},
    {'title': 'Teddy Picker', 'playback': '03:25',
     'artist': 'Arctic Monkeys'},
    {'title': 'Surfing With The Alien', 'playback': '04:34',
     'artist': 'Joe Satriani'}
]


def to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds


def longest_possible(playback):
    longest_song = 0
    song_title = ''
    for song in songs:
        song_length = to_seconds(song['playback'])
        if longest_song < song_length <= playback:
            longest_song = song_length
            song_title = song['title']
    return song_title or False

assert longest_possible(215) == 'For Reasons Unknown'
assert longest_possible(270) == 'YYZ'
assert longest_possible(13) is False
