def find_secret_number(low, high, guess_bot):
    while True:
        half = low + (high - low) // 2
        response = guess_bot.guess_number(half)
        if response == 'Correct':
            return half
        elif response == 'Larger':
            low = half + 1
        elif response == 'Smaller':
            high = half - 1
