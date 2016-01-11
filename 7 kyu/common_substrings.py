def substring_test(str1, str2):
    pass


assert substring_test("Something", "Home") is True
assert substring_test("Something", "Fun") is False
assert substring_test("Something", "") is False
assert substring_test("", "Something") is False
assert substring_test("BANANA", "banana") is True
assert substring_test("test", "lllt") is False
assert substring_test("", "") is False
assert substring_test("1234567", "541265") is True
assert substring_test("supercalifragilisticexpialidocious",
                      "SoundOfItIsAtrocious") is True
assert substring_test(
    "LoremipsumdolorsitametconsecteturadipiscingelitAeneannonaliquetligulaut"
    "placeratorciSuspendissepotentiMorbivolutpatauctoripsumegetaliquamPhasel"
    "lusidmagnaelitNullamerostellustemporquismolestieaornarevitaediamNullaal"
    "iquamrisusnonviverrasagittisInlaoreetultricespretiumVestibulumegetnulla"
    "tinciduntsempersemacrutrumfelisPraesentpurusarcutempusnecvariusidultric"
    "esaduiPellentesqueultriciesjustolobortisrhoncusdignissimNuncviverracons"
    "equatblanditUtbibendumatlacusactristiqueAliquamimperdietnuncsempertorto"
    "refficiturviverra", "thisisalongstringtest") is True
