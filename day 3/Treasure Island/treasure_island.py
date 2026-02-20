print("Welcome to Treasure Island")
print("Your Mission is to find the treasure.")


while True:
    choice1 = input('You are at a cross road. Type "left" or "right"\n').lower()
    
    if choice1 == "right":
        print("Game Over.\nYou fall inside a hole.")
        break
    elif choice1 == "left":
        print("You find a river.\n")
        break
    else:
        print("Please enter a valid choice.")

if choice1 == "left":
    while True:
        choice2 = input('Will you "wait" or "swim" to cross?\n').lower()
        
        if choice2 == "swim":
            print("Game Over.\nA shark eats you.")
            break
        elif choice2 == "wait":
            print("A boat arrives and you cross safely.\n")
            break
        else:
            print("Please enter a valid choice.")


if choice1 == "left" and choice2 == "wait":
    while True:
        choice3 = input('You see a dragon. "fight" or "hide"?\n').lower()
        
        if choice3 == "fight":
            print("The dragon eats you.\nGame Over.")
            break
        elif choice3 == "hide":
            print("The dragon falls asleep and you pass safely.\n")
            break
        else:
            print("Please enter a valid choice.")

if choice1 == "left" and choice2 == "wait" and choice3 == "hide":
    while True:
        choice4 = input('Two chests: "red" or "green"?\n').lower()
        
        if choice4 == "red":
            print("Game Over.\nA poisonous snake bites you.")
            break
        elif choice4 == "green":
            print("Congratulations! You win the game.")
            break
        else:
            print("Please enter a valid choice.")
