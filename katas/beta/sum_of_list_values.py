try:
    from builtins import sum as sum_list  # Python 3
except ImportError:
    from __builtin__ import sum as sum_list  # Python 2
