# Lab One
# Rothvitou Meng, Kiran Shahi
import random

def main():
    amount = 100
    queen = random.randint(1, 3)
    cards = ["Q","K","K"]
    print("|----------------------------|")
    print("|      THREE CARD MONTE      |")
    print("|----------------------------|")
    print("Find the queen to double your bet!")
    
    while True:
        print("You have $" + str(amount))
        try: 
            bet = int(input("How much you wanna bet? "))
            if bet > 0 and bet <= amount:
                amount -= bet
                print("You have $" + str(bet))
                print("Let's play!")
                print("+-----+ +-----+ +-----+")
                print("|     | |     | |     |")
                print("|  1  | |  2  | |  3  |")
                print("|     | |     | |     |")
                print("+-----+ +-----+ +-----+")
                guess = int(input(("Find the queen:")))
                print("+-----+ +-----+ +-----+")
                print("|     | |     | |     |")
                print("|  " + cards[0] + "  | |  " + cards[1] + "  | |  " + cards[2] + "  |")
                print("|     | |     | |     |")
                print("+-----+ +-----+ +-----+")
                
                if guess > 0 and guess <= 3:
                    if guess == queen:
                        print("You win!")
                        amount += bet
                    elif guess != queen:
                        print("Sorry... you lose!")
                else:
                    print("Invalid input - should be within range 1-3")
                    continue
                
                
            elif bet <=0 or bet > amount:
                print("Invalid input - should be within range 1-" + str(amount))
        except ValueError:
            print("Invalid input - should be an integer")
main()