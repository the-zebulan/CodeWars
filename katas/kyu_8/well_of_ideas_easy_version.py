def well(ideas):
    good_ideas = ideas.count('good')
    if good_ideas == 0:
        return 'Fail!'
    elif good_ideas < 3:
        return 'Publish!'
    return 'I smell a series!'
