def score_test(tests, right, omit, wrong):
    points = (right, omit, -wrong)
    return sum(points[test] for test in tests)
