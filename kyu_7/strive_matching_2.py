def match(job, candidates):
    job_equity = bool(job['equity_max'])
    job_locations = set(job['locations'])
    result = []
    for c in candidates:
        if not (c['desires_equity'] > job_equity) and \
                (c['current_location'] in job_locations or
                 job_locations.intersection(c['desired_locations'])):
            result.append(c)
    return result
