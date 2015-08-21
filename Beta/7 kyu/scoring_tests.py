def scoreTest(tests, right, omit, wrong):
    """ score_test == PEP8, forced mixedCase by CodeWars """
    points = (right, omit, -wrong)
    return sum(points[test] for test in tests)

assert scoreTest([0, 0, 0, 0, 2, 1, 0], 2, 0, 1) == 9
assert scoreTest([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2) == 3
