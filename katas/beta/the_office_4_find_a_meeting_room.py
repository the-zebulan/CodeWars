def meeting(rooms):
    try:
        return rooms.index('O')
    except ValueError:
        return 'None available!'
