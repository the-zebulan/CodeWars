from random import randint, seed

num = randint(1, 999)
seed(num)
guess = randint(1, 100)
seed(num)

assert randint(1, 100) == guess
