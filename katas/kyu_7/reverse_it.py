def reverse_it(data):
    if isinstance(data, (int, float, str)):
        return type(data)(str(data)[::-1])
    return data
