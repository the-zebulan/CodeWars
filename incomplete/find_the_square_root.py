import re

# re.findall(r'[A-Z]+[^A-Z]*', 'TheLongAndWindingRoad')


def to_camel_case(string_):
    pass


def to_snake_case(string_):
    # print re.split(r'([A-Z]+[a-z]*)', string_)

    # caps = re.findall(r'[A-Z]+[^A-Z]*', string_)
    caps = re.findall(r'[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][^A-Z]*', string_)
    # print caps
    if caps:
        return '_'.join(a.lower() for a in caps)
    return string_


print to_snake_case('')  # == ''

print to_snake_case('hello')  # == 'hello'
print to_snake_case('Router')  # == 'router'
print to_snake_case('URL')  # == 'url'

print to_snake_case('SnakeCase')  # == 'snake_case'
print to_snake_case('URLRouter')  # == 'url_router'
print to_snake_case('Impl0Test')  # == 'impl0_test'
print to_snake_case('CopyOnWriteArrayList')  # == 'copy_on_write_array_list'
print to_snake_case('API::V1::UserRegistrationController') \
     # == 'api::v1::user_registration_controller'

# print to_camel_case('')  # == ''
#
# print to_camel_case('hello')  # == 'Hello'
# print to_camel_case('Router')  # == 'Router'
# print to_camel_case('URL')  # == 'Url'
#
# print to_camel_case('camel_case')  # == 'CamelCase'
# print to_camel_case('url_router')  # == 'UrlRouter'
# print to_camel_case('copy_on_write_array_list')  # == 'CopyOnWriteArrayList'
# print to_camel_case('api::v1::user_registration_controller') \
#      # == 'Api::V1::UserRegistrationController'
