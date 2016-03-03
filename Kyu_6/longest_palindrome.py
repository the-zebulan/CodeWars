def longest_palindrome(s):
    length = len(s)
    for b in xrange(length, -1, -1):
        cnt = 0
        while cnt + b <= length:
            current = s[cnt:cnt + b]
            if current == current[::-1]:
                return b
            cnt += 1


assert longest_palindrome("a") == 1
assert longest_palindrome("aa") == 2
assert longest_palindrome("baa") == 2
assert longest_palindrome("aab") == 2
assert longest_palindrome("abcdefghba") == 1
assert longest_palindrome("baablkj12345432133d") == 9
assert longest_palindrome(
    'Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewna'
    'tionconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreate'
    'dequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranyna'
    'rtionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiem'
    'ldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingpla'
    'ceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfa'
    'ngandproperthatweshoulddothisButinalargersensewecannotdedicatewecannot'
    'consecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggle'
    'dherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadsw'
    'filllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhatthey'
    'didhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwh'
    'ichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobehered'
    'edicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetak'
    'eincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevo'
    'tionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthis'
    'nationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeople'
    'bythepeopleforthepeopleshallnotperishfromtheearth') == 7
