def acronym_buster(message):
    acronyms = {
        'CTA': 'call to action',
        'EOD': 'the end of the day',
        'IAM': 'in a meeting',
        'KPI': 'key performance indicators',
        'NRN': 'no reply necessary',
        'OOO': 'out of office',
        'SWOT': 'strengths, weaknesses, opportunities and threats',
        'TBD': 'to be decided',
        'WAH': 'work at home'
    }
    result = []
    for sentence in message.split('.'):
        tmp = []
        for i, word in enumerate(sentence.split()):
            if word.isupper() and len(word) > 2:
                try:
                    word = acronyms[word]
                except KeyError:
                    return ('{} is an acronym. I do not like acronyms. Please'
                            ' remove them from your email.'.format(word))
            tmp.append(word[0].upper() + word[1:] if i == 0 else word)
        result.append(' '.join(tmp))
    return '. '.join(result).rstrip()
