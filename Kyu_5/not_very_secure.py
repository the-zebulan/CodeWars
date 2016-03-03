alphanumeric = str.isalnum

assert alphanumeric("hello world_") is False
assert alphanumeric("PassW0rd") is True
assert alphanumeric("     ") is False
