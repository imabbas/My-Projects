# Aadil Abbas (aa4zw)

word = input('Enter a word: ')
word = word.upper()
length = len(word)
blank = ''
new_blank = ''
change = 0
turn = 6
final_blank = ''

for char in range(0,length):
    blank = blank + '-'

guess = input(('['+ (blank) + '] ' + 'You have ' + str(turn) + ' left, enter a letter: '))
guess = guess.upper()

while turn > 0:
    guess = guess.upper()
    if change == length:
        print('You win! The word was' + '"'+word+'"')
        break
    if guess not in word:
        turn = turn - 1
        if turn == 0:
            print('You lose! The word was' + '"'+word+'"')
            break
        print('Incorrect!')
        guess = input(('['+ blank + '] ' + 'You have ' + str(turn) + ' left, enter a letter: '))


    else:
        print('Correct!')
        index = 0
        temp_length = len(word)
        change = change + 1

        while index < temp_length:
            if guess == (word[index:index+1]):
                beginning = blank[0:index]
                end = blank[index+1:temp_length]
                blank = beginning + guess + end
            index += 1


        guess = input(('['+ blank + '] ' + 'You have ' + str(turn) + ' left, enter a letter: '))















