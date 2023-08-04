import random

def gameResult(computer, You):
    if computer == You:
        return None
    # COMPUTER CHOOSE SNAKE
    elif computer == 's':
        if You == 'w':
            return False

        elif You == 'g':
            return True

    # COMPUTER CHOOSE WATER
    elif computer == 'w':
        if You == 'g':
            return False

        elif You == 's':
            return True

    # COMPUTER CHOOSE GUN
    elif computer == 'g':
        if You == 's':
            return False

        elif You == 'w':
            return True


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'

You = input("Player's Turn: Snake(s) Water(w) or Gun(g)?")

b = gameResult(computer, You)
print(f"Computer choose {computer}")
print(f"Computer choose {You}")
if b == None:
    print("Game is Tie!")
elif b:
    print(f"You win! you choose {You} over {computer}")
else:
    print(f"You lose! You choose {You} over {computer}")