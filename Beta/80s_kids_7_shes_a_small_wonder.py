class Robot(object):
    def __init__(self):
        self.known_words = {
            'me', 'do', 'already', 'word', 'thank', 'for', 'i', 'understand',
            'know', 'teaching', 'not', 'input', 'the', 'you'}

    def learn_word(self, word):
        low = word.lower()
        if word.isalpha():
            if low in self.known_words:
                return 'I already know the word {}'.format(word)
            self.known_words.add(low)
            return 'Thank you for teaching me {}'.format(word)
        return 'I do not understand the input'


vicky = Robot()
assert vicky.learn_word('hello') == 'Thank you for teaching me hello'
assert vicky.learn_word('world') == 'Thank you for teaching me world'
assert vicky.learn_word('goodbye') == 'Thank you for teaching me goodbye'
assert vicky.learn_word('world') == 'I already know the word world'
assert vicky.learn_word('World') == 'I already know the word World'
assert vicky.learn_word('Thank') == 'I already know the word Thank'
