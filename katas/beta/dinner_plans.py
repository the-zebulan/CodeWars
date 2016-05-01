def common_ground(s1,s2):
    pass


print common_ground("eat chicken", "eat chicken and rice")  # == 'eat chicken'
print common_ground("eat a burger and drink a coke", "drink a coke")  # == 'drink a coke'
print common_ground("i like turtles", "what are you talking about")  # == 'death'
print common_ground("aa bb", "aa bb cc")  # == "aa bb"
print common_ground("aa bb cc", "bb cc")  # == 'bb cc'
print common_ground("aa bb cc", "bb cc bb aa")  # == 'bb cc aa'
print common_ground("aa bb", "cc dd")  # == 'death'
print common_ground("aa bb", "")  # == 'death'
print common_ground("", "cc dd")  # == 'death'
print common_ground("", "")  # == 'death'
