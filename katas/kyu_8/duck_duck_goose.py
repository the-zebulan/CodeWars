def duck_duck_goose(players, goose):
    return players[goose % len(players) - 1].name
