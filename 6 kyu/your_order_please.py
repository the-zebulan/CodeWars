def order(sentence):
    return ' '.join(sorted(sentence.split(),
                           key=lambda a: next(b for b in a if b.isdigit())))

# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda a: sorted(a)))

assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
