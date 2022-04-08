import random
from wsgiref.util import guess_scheme

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print("Lower")
        elif guess < random_number:
            print('Higer')
    print(f'Correct number was {random_number}')



def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'Is Number {guess} too high (H), Too low (L), or Correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("Yay!")

computerGuess(10)
