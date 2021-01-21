from random import choice


def round_winner(man_choice, pc_choice):
    if man_choice == 'rock':
        if pc_choice == 'rock':
            return 'tie'
        elif pc_choice == 'paper':
            return 'pc_choice'
        elif pc_choice == 'scissors':
            return 'man_choice'
    elif man_choice == 'paper':
        if pc_choice == 'rock':
            return 'man_choice'
        elif pc_choice == 'paper':
            return 'tie'
        elif pc_choice == 'scissors':
            return 'pc_choice'
    elif man_choice == 'scissors':
        if pc_choice == 'rock':
            return 'pc_choice'
        elif pc_choice == 'paper':
            return 'man_choice'
        elif pc_choice == 'scissors':
            return 'tie'


def play():
    options = ['rock', 'paper', 'scissors']

    pc_wins = 0
    man_wins = 0
    ties = 0
    total_rounds = 5
    print('Let\'s Play Rock Paper Scissors!')
    print('Total rounds:', total_rounds)
    man_choice = input('Choose between rock, paper and scissors: ').lower()
    while True:
        if man_choice in options:
            pc_choice = choice(options)
            winner = round_winner(man_choice, pc_choice)
            if winner == 'pc_choice':
                pc_wins += 1
                winner = 'Opponent'
            elif winner == 'man_choice':
                man_wins += 1
                winner = 'You'
            else:
                ties += 1
            total_rounds -= 1
            print(f'Your opponent choice:', pc_choice)
            if winner != 'tie':
                print(f'Round Winner:', winner)
            else:
                print('Tie Round')
            if total_rounds == 0:
                break
            print('Left Rounds:', total_rounds)
        else:
            print('Wrong Choice. Try Again\n')
        man_choice = input('Choose between rock, paper and scissors: ').lower()

    print('End of the game')
    print('Opponent won rounds', pc_wins)
    print('Your won rounds', man_wins)
    print('Tie rounds', ties)

    if pc_wins > man_wins:
        print('Opponent is the winner!')
    elif man_wins > pc_wins:
        print('You are the winner!')
    else:
        print('Tie Game!')


def main():
    play()
    while input('Wanna play again (Y/N) ? ').upper() == 'Y':
        play()


main()
