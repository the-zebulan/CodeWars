from os import uname


def get_pid():
    return uname()[1]

# Alternative: socket.gethostname()
