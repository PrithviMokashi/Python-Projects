import random

def guess(x):
    random_number = random.randint(1, x)
    value = 0
    while random_number != value:
        value = int(input(f"Guess a number from 1 to {x}\n"))
        if random_number > value:
            print("Nope, That's wrong try a higher number.")
        elif random_number < value:
            print("Nope, That's wrong try a lower number.")
    print(f"Excellent {random_number} is right.")

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    print(f"\n\n\nGuess a Number between 1 to {x}")
    while feedback != 'c':
        if low != high:
            value = random.randint(low, high)
        else:
            value = low #or high because low = high
        feedback = input(f"Is the guess {value} Too high(H), Too low(L) or Correct(C) : ").lower()
        if feedback == 'h':
            high = value - 1
        elif feedback == 'l':
            low = value + 1
    print(f"Excellent computer has guessed {value} correctly.")

guess(100)
computerGuess(1000)