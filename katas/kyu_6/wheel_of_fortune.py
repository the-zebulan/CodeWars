def winner(players):
    total_players = winner_name = winner_score = 0
    for p in players:
        try:
            name = p['name']
            scores = p['scores']
        except KeyError:
            return False
        score_total = total_spins = 0
        total_players += 1
        for score in scores:
            if score > 100 or score % 5:
                return False
            score_total += score
            total_spins += 1
        if score_total > 100:
            continue
        elif total_spins not in (1, 2):
            return False
        elif score_total > winner_score:
            winner_name = name
            winner_score = score_total
    return winner_name if winner_score and total_players == 3 else False
