# Lab One
# Rothvitou Meng, Kiran Shahi
import random
import check_input

def main():
    amount = 100

    print("|----------------------------|")
    print("|      THREE CARD MONTE      |")
    print("|----------------------------|")
    print("Find the queen to double your bet!")
    
    while True:
        print("You have $" + str(amount))
        bet = check_input.get_int_range("How much you wanna bet? ",1,amount)
        queen = random.randint(1,3)
        cards = ["K","K","K"]
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
        
        if guess == queen:
            print("You win!")
            amount += bet * 2

        else:
            print("Sorry... you lose!")
        print("You have $" + str(amount))
        if amount == 0:
            print("You are out of money!")
            print("Thanks for playing!")
            break

        choice = check_input.get_yes_no("Play again ...(Y/N): ")
        if not choice:
            print("Thanks for playing")
          
main()