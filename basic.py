# Group 1
# Name
# Desc

def main():
    print("Enter 5 numbers:")
    count = 0
    total = 0


    while count < 5:
        try: 
            val = int(input("Enter number: "))
            count += 1
            total += val
            if val <= 0:
                print("The number must be positive")
                continue
        except ValueError:
            print("Invalid number, Try again..")

    print("Sum = " + str(total))
    print("Average = " + str(total / count))


main()