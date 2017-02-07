
print('The Game of Nim')
print("")

marbles = int(input('Number of marbles are in the pile: '))
start = input('Who will start? (p or c): ')

if start == 'p':
    turn = True
else:
    turn = False
x = 10
new_pile = (2**x - 1)
computer_intake = 0
computer_marbles = 0

while marbles > 1:
    print('The pile has ' + str(marbles) + ' marbles in it.')
    while turn == True:
        max_marbles = int(marbles) // 2
        player_marbles = 0
        player_intake = 0
        while player_intake < 1 or player_intake > max_marbles:
            player_intake = int(input('How many marbles do you want to take?' + '(1-'+ str(max_marbles) + '):'))
            if player_intake >= 1 and player_intake <= max_marbles:
                        player_marbles = player_marbles + player_intake
                        marbles = marbles - player_marbles
                        print('The pile has ' + str(marbles) + ' marbles in it.')
                        turn = False
    while turn == False:
        final_intake = 0


        max_marbles = int(marbles) // 2

        computer_intake = max_marbles


        while not turn:


            for computer_intake in range(max_marbles, 0, -1):
                for x in range(10,0,-1):
                    if marbles - computer_intake == ((2**x)-1):
                        final_intake = final_intake + computer_intake
                    if computer_intake > marbles//2:
                        computer_intake = 1
            print('The computer takes ' + str(final_intake) + ' marbles.')
            marbles = marbles - final_intake
            turn = True












