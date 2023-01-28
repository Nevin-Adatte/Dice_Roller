import random
while True:
    dice = input("Roll the dice(y/n): ")
    if dice == "y":
        n = random.randint(1,6)
        print("Value on the dice is " + str(n))
        if n == 1:
            print(" ______")
            print("|      |")
            print("|      |")
            print("|   o  |")
            print("|      |")
            print("|______|")
        elif n == 2:
            print(" ______")
            print("|      |")
            print("| o    |")
            print("|      |")
            print("|     o|")
            print("|______|")
        elif n == 3:
            print(" ______")
            print("|      |")
            print("| o    |")
            print("|   o  |")
            print("|     o|")
            print("|______|")
        elif n == 4:
            print(" ______")
            print("|      |")
            print("| o   o|")
            print("|      |")
            print("| o   o|")
            print("|______|")
        elif n == 5:
            print(" ______")
            print("|      |")
            print("| o   o|")
            print("|   o  |")
            print("| o   o|")
            print("|______|")
        else:
            print(" ______")
            print("|      |")
            print("| o   o|")
            print("| o   o|")
            print("| o   o|")
            print("|______|")
    elif dice == "n":
        break;
    else:
        print("Invalid selection")
