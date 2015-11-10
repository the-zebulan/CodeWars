def unscramble_eggs(word):
    return word.replace('egg', '')


assert unscramble_eggs("Beggegeggineggneggeregg") == 'Beginner'
assert unscramble_eggs("ceggodegge heggeregge") == "code here"
assert unscramble_eggs("FeggUNegg KeggATeggA") == "FUN KATA"
