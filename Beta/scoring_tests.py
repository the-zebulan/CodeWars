def score_test(tests, right, omit, wrong):
    points = (right, omit, -wrong)
    return sum(points[test] for test in tests)

assert score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1) == 9
assert score_test([0, 1, 0, 0, 2, 1, 0, 2, 2, 1], 3, -1, 2) == 3
