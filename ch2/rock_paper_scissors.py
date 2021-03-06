import random
import sys

print('Rock, Paper, Scissors')

# These variables keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop
        print('Type one of r, p, s, or q')

    # Display what the player chose
    if player_move == 'r':
        print('Rock vs. ')
    elif player_move == 'p':
        print('Paper vs. ')
    elif player_move == 's':
        print('Scissors vs. ')
    # todo In PyCharm, if you start a comment with "todo", PyCharm creates a to-do list item. Nice, remember this!

    # Display what the computer chose
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = 'r'
        print('Rock')
    elif random_num == 2:
        computer_move = 'p'
        print('Paper')
    elif random_num == 3:
        computer_move = 's'
        print('Scissors')

    # Display and record who wins and loses. This section also keeps score.
    if player_move == computer_move:
        print("TIE!")
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('WINNER!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('WINNER!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('WINNER')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('LOSER!')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('LOSER!')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('LOSER!')
        losses += 1
