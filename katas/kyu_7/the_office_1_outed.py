def outed(meet, boss):
    result = (sum(meet.values()) + meet[boss]) / len(meet)
    return 'Nice Work Champ!' if result > 5 else 'Get Out Now!'
