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
