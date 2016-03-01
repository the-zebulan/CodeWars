def leo(oscar):
    if oscar <= 88:
        return {86: 'Not even for Wolf of wallstreet?!',
                88: 'Leo finally won the oscar! Leo is happy'}.get(
            oscar, 'When will you give Leo an Oscar?')
    return 'Leo got one already!'


assert leo(88) == 'Leo finally won the oscar! Leo is happy'
assert leo(86) == 'Not even for Wolf of wallstreet?!'
assert leo(20) == 'When will you give Leo an Oscar?'
assert leo(90) == 'Leo got one already!'
