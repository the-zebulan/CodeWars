name = input('What is your name? ')
x_print('Hello {}!'.format(name))

quest = input('What is your quest? ')
x_print('Your quest: {}'.format(quest))

num_books = int(input('How many books do you own? '))
book_weight = float(input('What is the weight of the average book? '))
total_weight = num_books * book_weight
x_print('The total weight for {} books is: {}'.format(num_books, total_weight))
