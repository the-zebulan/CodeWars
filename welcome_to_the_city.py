def say_hello(name, city, state):
    return 'Hello, {}! Welcome to {}, {}!'.format(' '.join(name), city, state)

assert say_hello(['John', 'Smith'], 'Phoenix', 'Arizona') ==  'Hello, John Smith! Welcome to Phoenix, Arizona!','Hello, John Smith! Welcome to Phoenix, Arizona!'
assert say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois') == 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!'
assert say_hello(['Wallace','Russel','Osbourne'],'Albany','New York') == 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!'
