def substring_test(*args):
    shorter, longer = sorted((a.lower() for a in args), key=len)
    length = len(shorter) + 1
    for b in xrange(2, length):
        for c in xrange(length - b):
            if longer.find(shorter[c:c + b]) != -1:
                return True
    return False


assert substring_test('Something', 'Home') is True
assert substring_test('Something', 'Fun') is False
assert substring_test('Something', '') is False
assert substring_test('', 'Something') is False
assert substring_test('BANANA', 'banana') is True
assert substring_test('test', 'lllt') is False
assert substring_test('', '') is False
assert substring_test('1234567', '541265') is True
assert substring_test('Codewars is sweet!', 'is') is True
assert substring_test('supercalifragilisticexpialidocious',
                      'SoundOfItIsAtrocious') is True
assert substring_test(
    'LoremipsumdolorsitametconsecteturadipiscingelitAeneannonaliquetligulaut'
    'placeratorciSuspendissepotentiMorbivolutpatauctoripsumegetaliquamPhasel'
    'lusidmagnaelitNullamerostellustemporquismolestieaornarevitaediamNullaal'
    'iquamrisusnonviverrasagittisInlaoreetultricespretiumVestibulumegetnulla'
    'tinciduntsempersemacrutrumfelisPraesentpurusarcutempusnecvariusidultric'
    'esaduiPellentesqueultriciesjustolobortisrhoncusdignissimNuncviverracons'
    'equatblanditUtbibendumatlacusactristiqueAliquamimperdietnuncsempertorto'
    'refficiturviverra', 'thisisalongstringtest') is True
