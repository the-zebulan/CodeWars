def clock_degree(clock_time):
    hour, minutes = (int(a) for a in clock_time.split(':'))
    if not (24 > hour >= 0 and 60 > minutes >= 0):
        return 'Check your time !'
    return '{}:{}'.format((hour % 12) * 30 or 360, minutes * 6 or 360)
