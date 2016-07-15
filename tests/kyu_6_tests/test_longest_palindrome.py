import unittest

from katas.kyu_6.longest_palindrome import longest_palindrome


class LongestPalindromeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(longest_palindrome("a"), 1)

    def test_equals_2(self):
        self.assertEqual(longest_palindrome("aa"), 2)

    def test_equals_3(self):
        self.assertEqual(longest_palindrome("baa"), 2)

    def test_equals_4(self):
        self.assertEqual(longest_palindrome("aab"), 2)

    def test_equals_5(self):
        self.assertEqual(longest_palindrome("abcdefghba"), 1)

    def test_equals_6(self):
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)

    def test_equals_7(self):
        self.assertEqual(longest_palindrome(
            'Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainen'
            'tanewnationconceivedinzLibertyanddedicatedtothepropositionthata'
            'llmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhet'
            'herthatnaptionoranynartionsoconceivedandsodedicatedcanlongendur'
            'eWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateap'
            'ortionofthatfieldasafinalrestingplaceforthosewhoheregavetheirli'
            'vesthatthatnationmightliveItisaltogetherfangandproperthatweshou'
            'lddothisButinalargersensewecannotdedicatewecannotconsecrateweca'
            'nnothallowthisgroundThebravelmenlivinganddeadwhostruggledhereha'
            'veconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadsw'
            'filllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetw'
            'hattheydidhereItisforusthelivingrathertobededicatedheretotheuln'
            'finishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedIti'
            'sratherforustobeherededicatedtothegreattdafskremainingbeforeust'
            'hatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhi'
            'chtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvet'
            'hatthesedeadshallnothavediedinvainthatthisnationunsderGodshallh'
            'aveanewbirthoffreedomandthatgovernmentofthepeoplebythepeoplefor'
            'thepeopleshallnotperishfromtheearth'), 7
        )
