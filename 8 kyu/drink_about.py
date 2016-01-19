def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:
        return 'drink beer'
    return 'drink whisky'


assert people_with_age_drink(13) == "drink toddy"
assert people_with_age_drink(17) == "drink coke"
assert people_with_age_drink(18) == "drink beer"
assert people_with_age_drink(20) == "drink beer"
assert people_with_age_drink(30) == "drink whisky"
