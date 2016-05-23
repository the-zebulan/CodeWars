def scoreboard(who_ate_what):
    scores = {'chickenwings': 5, 'hamburgers': 3, 'hotdogs': 2}
    return sorted((
        {'name': a.pop('name'),
         'score': sum(scores.get(k, 0) * v for k, v in a.iteritems())}
        for a in who_ate_what), key=lambda b: (-b['score'], b['name']))
