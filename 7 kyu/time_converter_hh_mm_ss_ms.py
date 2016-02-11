from datetime import datetime


def convert(time):
    return '{:02}:{:02}:{:02},{:03}'.format(
        time.hour, time.minute, time.second, time.microsecond / 1000)


assert convert(datetime(2016, 2, 8, 16, 42, 59)) == '16:42:59,000'
assert convert(datetime(1951, 10, 31, 2, 2, 24, 399000)) == '02:02:24,399'
assert convert(datetime(1523, 5, 29, 23, 2, 2, 9000)) == '23:02:02,009'
assert convert(datetime(1, 1, 1, 1, 1, 1, 110000)) == '01:01:01,110'
assert convert(datetime(9999, 9, 9, 9, 9, 9, 999999)) == '09:09:09,999'
assert convert(datetime(2, 12, 30, 23, 59, 59, 875939)) == '23:59:59,875'
assert convert(datetime(1850, 12, 30, 13, 39, 19)) == '13:39:19,000'
assert convert(datetime(1978, 3, 18, 12, 0, 0, 0)) == '12:00:00,000'
assert convert(datetime(1850, 12, 30, 11, 11, 11, 123939)) == '11:11:11,123'
assert convert(datetime(1850, 12, 30, 0, 0, 0, 321939)) == '00:00:00,321'
