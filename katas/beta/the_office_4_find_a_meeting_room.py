def meeting(rooms):
    return next((i for i, a in enumerate(rooms) if a == 'O'), None)
