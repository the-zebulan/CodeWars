from re import match


def validate_pin(pin):
    return bool(match(r'(\d{4}|\d{6})$', pin))
