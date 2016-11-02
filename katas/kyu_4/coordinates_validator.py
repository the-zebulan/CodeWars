def is_valid_coordinates(coordinates):
    try:
        latitude, longitude = (
            abs(float(a)) for a in coordinates.split(', ') if 'e' not in a)
    except ValueError:
        return False
    return latitude <= 90 and longitude <= 180
