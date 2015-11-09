from string import ascii_uppercase


def get_best_word(points, words):
    letter_score = dict(zip(ascii_uppercase, points))
    max_score = max_word_index = max_word_length = 0
    for i, word in enumerate(words):
        current_score = current_length = 0
        for a in word:
            current_length += 1
            current_score += letter_score[a]
        if current_score > max_score:
            max_score = current_score
            max_word_index = i
            max_word_length = current_length
        elif current_score == max_score and max_word_length > current_length:
            max_word_index = i
            max_word_length = current_length
    return max_word_index


points = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1, 2, 1,
          1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10)
assert get_best_word(points, ["WHO", "IS", "THE", "BEST", "OF", "US"]) == 0
assert get_best_word(points,
                     ["NOQ", "TXAY", "S", "OM", "ESFT", "CJUKQ", "QL", "QO",
                      "ASTK", "Y"]) == 5
assert get_best_word(points,
                     ["N", "AO", "TQGZW", "P", "OBTP", "CLWXB", "Y", "JQGFJ",
                      "Q", "RP", "OC", "MRQCZ", "ZWN", "ZRT", "OIRYH",
                      "GWPMSZP", "LQRYUKQ", "LBM", "LFEI", "VHUX", "RTALLIC",
                      "JEMUPS", "XUW", "X", "ZLXFMWS", "LFAGR", "HJ", "RTUAI",
                      "JRBNG", "ZUYSC", "CIEYV", "FUY", "B", "EJS", "CINBTQS",
                      "JEAC", "JX", "LLILSEK", "W", "KLUV"]) == 16
assert get_best_word(points,
                     ["SVWLIDP", "FCPKTHW", "EREMN", "NFEF", "PQ", "FSC",
                      "ZYPOSXJ", "BOR", "YCGG", "RC", "DVPE", "VAOE", "OIGK",
                      "OTQE", "REJFUFD", "FVBCSSB", "VHJ", "BEC", "MWZQ", "WX",
                      "L", "ZPCB", "JKLHE", "RYFTY", "NKP", "ID", "O", "KA",
                      "VRXX", "NTDB", "OERKPC", "YFLUI", "SKQCJ", "PXDSW",
                      "ITYWD", "TC", "LOIDQEJ", "NE", "YND", "VJHOCEC",
                      "RPRANZ", "BQ", "STM", "RGVBFW", "SMWUYLW", "KT", "SXHY",
                      "XCE", "T", "SC", "UDJU", "CHDR", "UGXNQ", "CQOOBA", "O",
                      "NWW", "V", "L", "BAQ", "AZN", "LBTR", "N", "QSURR",
                      "KADPH", "M", "LCBEAKM", "ZHEVXS", "F", "TVAIQCY", "MF",
                      "KCI", "YQ", "RCG", "AKYPCP", "WJXG", "RQXOI", "SJI",
                      "TWXZ", "J", "HIKCGHV", "EAAXGG", "AETSH", "EO", "BUET",
                      "TDIQCO", "TKL", "FJCRY", "ZHAJLK", "OLMCVA", "F"]) == 6
assert get_best_word(points,
                     ["RBBL", "ZJ", "ZOFXE", "LMBFCFX", "O", "JG", "SYRYE",
                      "VXG", "EU", "DAIFZR", "BQUNZHH", "WKO", "TFPHPLX",
                      "SWLG", "CY", "JYQNDSM", "ITPS", "B", "UVSDMWR",
                      "LCPS"]) == 15
assert get_best_word(points,
                     ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO',
                      'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']) == 5
