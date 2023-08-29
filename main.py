# Melody Gatan, Kenton La
# 09/29/2023
# three card monte gambling addiction go crazy

import random
    
# get user's bet amount within the available money range
def get_users_bet(money):
    print(f'You have ${money}.')
    valid = False
    while not valid:
        try:
            bet = int(input('How much you wanna bet? '))
            if money >= bet > 0:
                valid = True
            else:
                print(f'Invalid input - should be within range 1-{money}.')
        except ValueError:
            print('Invalid input - should be an integer.')
    return bet

# get user's card choice (1, 2, or 3)
def get_users_choice():
    valid = False
    while not valid:
        try:
            choice = int(input('Find the queen: '))
            if choice >= 1 and choice <= 3:
                valid = True
            else:
                print(f'Invalid input - should be within range 1-3.')
        except ValueError:
            print('Invalid input - should be an integer.')
    return choice

# Display the cards with the queen's location
def display_queen_loc(queen_loc):
    template =(
            "+-----+ +-----+ +-----+\n"
            "|     | |     | |     |\n"
           "|  {}  | |  {}  | |  {}  |\n"
            "|     | |     | |     |\n"
            "+-----+ +-----+ +-----+"
            )
    cards = ["K", "K", "K"]
    cards[queen_loc - 1] = "Q"
    # print(cards)
    card_display = template.format(cards[0], cards[1], cards[2])
    print(card_display)

        
#main game loop
def main():
    money = 100
    queen_loc = 0
    user_choice = 1
    print('-Three card Monte-\nFind the queen to double your bet!\n')
    while True:
        queen_loc = random.randint(1,3)
        bet = get_users_bet(money)
        user_choice = get_users_choice()
        display_queen_loc(queen_loc)
        money -= bet
        if user_choice == queen_loc:
            print('You got lucky this time...')
            money += bet * 2
        else:
            print('Sorry... you lose.')
        if money == 0:
            print('You\'re out of money. Beat it loser!')
            return False
        play = input('Play again? (Y/N): ')
        if play != 'y':
            return False
        
#start the game
main()