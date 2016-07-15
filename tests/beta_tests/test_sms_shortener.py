import unittest

from katas.beta.sms_shortener import shortener


class ShortenerTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(shortener(
            'No one expects the Spanish Inquisition! Our chief weapon is '
            'surprise, fear and surprise; two chief weapons, fear, surpri'
            'se, and ruthless efficiency! And that will be it.'),
            'No one expects the Spanish Inquisition! Our chief weapon is s'
            'urprise, fear and surprise; two chief weapons, fear,Surprise,'
            'AndRuthlessEfficiency!AndThatWillBeIt.')

    def test_equal_2(self):
        self.assertEqual(shortener(
            'SMS messages are limited to 160 characters. It tends to be ir'
            'ritating, especially when freshly written message is 164 char'
            'acters long. SMS messages are limited to 160 characters. It t'
            'ends to be irritating, especially when freshly written messag'
            'e is 164 characters long.'),
            'SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,Es'
            'peciallyWhenFreshlyWrittenMessageIs164CharactersLong.SMSMessa'
            'gesAreLimitedTo160Characters.ItTendsToBeIrritating,Especially'
            'WhenFreshlyWrittenMessageIs164CharactersLong.')

    def test_equal_3(self):
        self.assertEqual(shortener(
            'here is my message here is my message here is my message here '
            'is my message here is my message!'
        ), 'here is my message here is my message here is my message here '
           'is my message here is my message!')

    def test_equal_4(self):
        self.assertEqual(shortener(
            'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijab'
            'cdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij'
        ), 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabc'
           'defghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij')
