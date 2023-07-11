def treausure_island():
    print("Welcome to Treasure island.\nYour mission is to find the treasure.")
    left_right = input("left or right ")
    if left_right.lower() == "left":
        swim_wait = input("swim or wait ")
        if swim_wait == "swim":
            which_dorr = input("Which door?\nRed\nBlue\nYellow\n")
            if which_dorr.lower() == "red":
                print("Game over")
            elif which_dorr.lower() == 'blue':
                print("Game over")
            elif which_dorr.lower() == "yellow":
                print("You win ")
            else:
                print("My man learn how to type 1st grade colours")
        else:
            print("motherfc")
    else:
        print("You lost")


treausure_island()
