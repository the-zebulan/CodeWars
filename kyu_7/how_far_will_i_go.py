def travel(total_time, run_time, rest_time, speed):
    q, r = divmod(total_time, run_time + rest_time)
    return (q * run_time + min(r, run_time)) * speed
