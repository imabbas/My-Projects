# Aadil Abbas (aa4zw)

import random

number = int(input('What should the answer be? '))

if number == -1:
        number = random.randint(0, 100)



guess = int(input('Guess a number: '))
x = 0
while x <= 4:
    x = x + 1
    if guess > number:
        print('The number is lower than that.')
        guess = int(input('Guess a number: '))
    if guess < number:
        print('The number is higher than that.')
        guess = int(input('Guess a number: '))
    if guess == number:
        print('You win!')
        break


    if x == 4:
        print("You lose; the number was " + str(number) + '.')
        break





