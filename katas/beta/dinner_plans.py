def common_ground(s1,s2):
    words = s2.split()
    return ' '.join(sorted((a for a in set(s1.split()) if a in words),
                           key=lambda b: words.index(b))) or 'death'
