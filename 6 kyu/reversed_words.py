def reverseWords(string):
    """ reverse_words == PEP8 (forced mixedCase by CodeWars) """
    return ' '.join(reversed(string.split()))

assert reverseWords('The greatest victory is that which requires no battle') \
       == 'battle no requires which that is victory greatest The'
assert reverseWords('hello world!') == 'world! hello'
