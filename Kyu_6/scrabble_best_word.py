from string import ascii_uppercase


def get_best_word(points, words):
    letter_score = dict(zip(ascii_uppercase, points))
    max_score = max_word_index = max_word_length = 0
    for i, word in enumerate(words):
        current_score = current_length = 0
        for a in word:
            current_length += 1
            current_score += letter_score[a]
        if current_score > max_score:
            max_score = current_score
            max_word_index = i
            max_word_length = current_length
        elif current_score == max_score and max_word_length > current_length:
            max_word_index = i
            max_word_length = current_length
    return max_word_index
