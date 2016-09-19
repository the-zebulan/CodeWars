def presentation_agenda(people):
    result = []
    for i, person in enumerate(people):
        destinations = set(person['dest'])
        for j, audience_member in enumerate(people):
            if i == j:
                continue
            destinations.difference_update(audience_member['dest'])
        if destinations:
            result.append({'person': person['person'],
                           'dest': sorted(destinations)})
    return result
