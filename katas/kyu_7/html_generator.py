HTML_TAG = '<{0}>{1}</{0}>'.format


class HTMLGen:
    @staticmethod
    def comment(text):
        return '<!--{}-->'.format(text)

    @staticmethod
    def a(text):
        return HTML_TAG('a', text)

    @staticmethod
    def b(text):
        return HTML_TAG('b', text)

    @staticmethod
    def p(text):
        return HTML_TAG('p', text)

    @staticmethod
    def body(text):
        return HTML_TAG('body', text)

    @staticmethod
    def div(text):
        return HTML_TAG('div', text)

    @staticmethod
    def span(text):
        return HTML_TAG('span', text)

    @staticmethod
    def title(text):
        return HTML_TAG('title', text)
