import unittest

from Beta.sms_shortener import shortener


class ShortenerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shortener(
            'No one expects the Spanish Inquisition! Our chief weapon is '
            'surprise, fear and surprise; two chief weapons, fear, surpri'
            'se, and ruthless efficiency! And that will be it.'),
            'No one expects the Spanish Inquisition! Our chief weapon is s'
            'urprise, fear and surprise; two chief weapons, fear,Surprise,'
            'AndRuthlessEfficiency!AndThatWillBeIt.')

    def test_equals_2(self):
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


if __name__ == '__main__':
    unittest.main()
