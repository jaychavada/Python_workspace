# Generate random number

import random

rnum = random.randint(1, 5)
print(rnum)
userGuess = None
guesses = 0
while (userGuess != rnum):
    userGuess = int(input("Enter Your guess: "))
    if (userGuess == rnum):
        print("You guessed it right!")
    else:
        if(userGuess>rnum):
            print("You guessed it wrong! Enter smaller number")
        else:
            print("You guessed it wrong! Enter larger number")
    guesses += 1

print(f"You guessed the number in {guesses} guesses")