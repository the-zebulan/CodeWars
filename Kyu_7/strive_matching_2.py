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


candidates = [{
    'desires_equity': True,
    'current_location': 'New York',
    'desired_locations': ['San Francisco', 'Los Angeles']
    }, {
    'desires_equity': False,
    'current_location': 'San Francisco',
    'desired_locations': ['Kentucky', 'New Mexico']
}]
job1 = {'equity_max': 0, 'locations': ['Los Angeles', 'New York']}
job2 = {'equity_max': 1.2, 'locations': ['New York', 'Kentucky']}
assert len(match(job1, candidates)) == 0
assert len(match(job2, candidates)) == 2
