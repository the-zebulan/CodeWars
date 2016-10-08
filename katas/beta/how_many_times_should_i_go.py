from math import ceil
from operator import truediv


def how_many_times(annual_price, individual_price):
    return int(ceil(truediv(annual_price, individual_price)))
