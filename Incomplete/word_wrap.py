import textwrap
import re


def word_wrap(string, width):
    lines = []
    for paragraph in string.split('\n'):
        line = []
        len_line = 0
        for word in paragraph.split(' '):
            len_word = len(word)
            if len_line + len_word <= width:
                line.append(word)
                len_line += len_word + 1
            else:
                lines.append(' '.join(line))
                line = [word]
                len_line = len_word + 1
        lines.append(' '.join(line))
    return '\n'.join(lines)

    # # lim=75
    # for s in string.split("\n"):
    #     if s == "":
    #         print
    #     w = 0
    #     l = []
    #     for d in s.split():
    #         if w + len(d) + 1 <= width:
    #             l.append(d)
    #             w += len(d) + 1
    #         else:
    #             print " ".join(l)
    #             l = [d]
    #             w = len(d)
    #     if len(l):
    #         print " ".join(l)
    # return ''

    # words = []
    # # lines = []
    # # line = []
    # # line_cnt = 0
    # for word in string.split():
    #     length = len(word)
    #     if length <= width:
    #         # words.append((word, length))
    #         words.append(word)
    #         # + 1 word
    #     else:
    #         for a in range(0, length, width):
    #             words.append(word[a:a + width])
    #             # chunk = word[a:a + width]
    #             # words.append((chunk, len(chunk)))
    #             # + 1 word
    # print(words)
    # total_words = len(words)  # save this by counting above
    # result = []
    # start_dex = 0
    # end_dex = 2
    # while end_dex < total_words:
    #     current = ' '.join(words[start_dex:end_dex])
    #     if len(current) == width:
    #         result.append(current)
    #         start_dex = end_dex
    #         end_dex += 2
    #     elif len(current) > width:
    #         result.append(' '.join(words[start_dex:end_dex - 1]))
    #         start_dex = end_dex - 1
    #         end_dex += 2
    #     end_dex += 1
    # return '\n'.join(result)


print word_wrap("test", 7)  # == "test"
print word_wrap("hello world", 7)  # == "hello\nworld"
print word_wrap("a lot of words for a single line", 10)  # \
# == "a lot of\nwords for\na single\nline"
print word_wrap("areallylongword", 6)
# print fill('areallylongword', 6)

# print textwrap.fill('thestringislong', 6)
# print textwrap.fill('what if there are separate words', 6)
