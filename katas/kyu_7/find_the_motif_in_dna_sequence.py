def motif_locator(seq, motif):
    dex = 0
    result = []
    while True:
        dex = seq.find(motif, dex)
        if dex == -1:
            return result
        dex += 1
        result.append(dex)
