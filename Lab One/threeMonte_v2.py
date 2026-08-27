# Lab One | Three Monte Card
# Rothvitou Meng, Kiran Shahi
# Lab 17 
# Description:
# This program simulates a Three Card Monte game.
# The player starts with $100, places a bet, and guesses
# which card contains the queen. The game continues until
# the player chooses to stop or runs out of money.
import random
import check_input

def main():
    # Inilize with 100$
    amount = 100

    print("|----------------------------|")
    print("|      THREE CARD MONTE      |")
    print("|----------------------------|")
    print("Find the queen to double your bet!")
    
    while True:
        print("You have $" + str(amount))
        bet = check_input.get_int_range("How much you wanna bet? ",1,amount)
        # Randomize the queen's positive in range of 1 and 3
        queen = random.randint(1,3)
        cards = ["K","K","K"]
        # Display the card's queen position
        cards[queen - 1] = "Q"
        print("You have $" + str(amount))
        print("Let's play!")
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  1  | |  2  | |  3  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        guess = check_input.get_int_range("Find the queen: ",1,3)
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  " + cards[0] + "  | |  " + cards[1] + "  | |  " + cards[2] + "  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
        
        # Algorithm to check guess and queen 
        if guess == queen:
            print("You win!")
            amount += bet * 2
        else:
            print("Sorry... you lose!")
        print("You have $" + str(amount))
        if amount <= 0:
            print("You are out of money!")
            print("Thanks for playing!")
            break

        play = check_input.get_yes_no("Play again ...(Y/N): ")
        if not play:
            print("Thanks for playing")
          
main()