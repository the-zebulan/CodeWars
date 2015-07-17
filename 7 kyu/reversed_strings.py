def solution(string):
    return string[::-1]

assert solution('world') == 'dlrow'
assert solution('hello') == 'olleh'
assert solution('') == ''
assert solution('h') == 'h'
