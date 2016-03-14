def order(sentence):
    return ' '.join(sorted(sentence.split(),
                           key=lambda a: next(b for b in a if b.isdigit())))

# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda a: sorted(a)))
