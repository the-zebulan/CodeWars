def is_valid_coordinates(coordinates):
    valid_chars = set('0123456789-.')
    try:
        latitude, longitude = (float(a) for a in coordinates.split(', ')
                               if valid_chars.issuperset(a))
    except ValueError:
        return False
    return -90 <= latitude <= 90 and -180 <= longitude <= 180
