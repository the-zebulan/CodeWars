def arrange(strng):
    result = []
    words = [(a, len(a)) for a in strng.split()]
    print words
    length = len(words)
    less_than = True
    # for a in xrange(length):
    #     l_word, l_len = words[a]
    #     print
    #     for b in xrange(a + 1, length):
    #         r_word, r_len = words[b]
    #         print 'left: {}\tright: {}\tless_than: {}'\
    #             .format(l_word, r_word, less_than)
    #         if less_than:
    #             if l_len <= r_len:
    #                 words.insert(a + 1, words.pop(b))  # skip if a + 1 == b
    #                 break
    #         else:
    #             pass
    #             # if l_len >= r_len:
    #             #     words.insert(a + 1, words.pop(b))
    #             #     break
    #     print ' '.join(c[0] for c in words)
    #     less_than = not(less_than)
    # print


print arrange("who hit retaining The That a we taken")  # == "who RETAINING hit THAT a THE we TAKEN"  # 3
# print arrange("on I came up were so grandmothers")  # == "i CAME on WERE up GRANDMOTHERS so"  # 4
# print arrange("way the my wall them him")  # == "way THE my WALL him THEM"  # 1
# print arrange("turn know great-aunts aunt look A to back")  # == "turn GREAT-AUNTS know AUNT a LOOK to BACK"  # 2
