class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type

assert Ball().ball_type == 'regular'
assert Ball('super').ball_type == 'super'
