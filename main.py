# Kenton La, Melody Gatan
# 8/29/2023
# Have a user enter their bet and lets them choose a card for a chance to double their money
import random


def main():
    money = 100
    print('-Three card Monte-\nFind the queen to double your bet!\n')
    end = False
    while not end:
        queen_loc = random.randint(1, 3)
        bet = get_user_bet(money)
        choice = get_user_choice()
        display_queen_loc(queen_loc)
        if choice == queen_loc:
            print('You got lucky this time...')
            money += bet
        else:
            print('Sorry... you lose.')
            money -= bet
        if money == 0:
            print("You're out of money. Beat it loser!")
            end = True
        else:
            valid = False
            while not valid:
                play_again = input('Play again? (Y/N): ')
                if play_again.lower() == 'n':
                    end = True
                    valid = True
                elif play_again.lower() == 'y':
                    end = False
                    valid = True
                else:
                    print('Invalid Input - should be Y/N')




def get_user_bet(money):
    print(f'You have ${money}.')
    valid = False
    while not valid:
        try:
            bet = int(input('How much do you wanna bet? '))
            if money >= bet > 0:
                return bet
            else:
                print(f'Invalid input - should be within range 1-{money}.')
        except ValueError:
            print('Invalid input - should be an integer.')


def get_user_choice():
    template = (
        "+-----+ +-----+ +-----+\n"
        "|     | |     | |     |\n"
        "|  1  | |  2  | |  3  |\n"
        "|     | |     | |     |\n"
        "+-----+ +-----+ +-----+"
    )
    print(template)
    valid = False
    while not valid:
        try:
            queen_loc = int(input('Find the queen: '))
            if 1 <= queen_loc <= 3:
                return queen_loc
            else:
                print(f'Invalid input - should be within range 1-3.')
        except ValueError:
            print('Invalid input - should be an integer.')


def display_queen_loc(queen_loc):
    top_card = "+-----+ +-----+ +-----+\n|     | |     | |     |"
    bottom_card = "|     | |     | |     |\n+-----+ +-----+ +-----+"

    print(top_card)
    if queen_loc == 1:
        print("|  Q  | |  K  | |  K  |")
    elif queen_loc == 2:
        print("|  K  | |  Q  | |  K  |")
    else:
        print("|  K  | |  K  | |  Q  |")
    print(bottom_card)


main()