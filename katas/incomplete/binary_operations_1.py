def flip_bit(num, dex):
    return num ^ (1 << dex)


print flip_bit(15, 4)
