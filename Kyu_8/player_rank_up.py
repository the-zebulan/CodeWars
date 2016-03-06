MSG = "Well done! You have advanced to the qualifying stage. " \
      "Win 2 out of your next 3 games to rank up."


def playerRankUp(pts):
    """ player_rank_up == PEP8 (forced mixedCase by CodeWars) """
    return False if pts < 100 else MSG
