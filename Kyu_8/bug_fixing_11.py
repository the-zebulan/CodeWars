USERS = (
    {'username': 'Timmy', 'password': 'password'},
    {'username': 'Johny', 'password': 'Hf7FAbf6'},
    {'username': 'Alice', 'password': 'alice'},
    {'username': 'Roger', 'password': 'pass'},
    {'username': 'Simon', 'password': 'says'},
    {'username': 'Admin', 'password': 'ads78adsg7dasga'}
)


class Validator(object):  # Validator class is hidden in this kata
    @staticmethod
    def login(username, password):
        for user in USERS:
            if user['username'] == username and user['password'] == password:
                return 'Successfully Logged in!'
        return 'Wrong username or password!'


# solution is below this line
def validate(username, password):
    return Validator().login(username, password)
