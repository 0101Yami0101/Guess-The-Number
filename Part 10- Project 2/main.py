#Find the randomly generated number between 1-1000 with the minimum number of guesses


import random 
randomno = random.randint(1,1000)
# print(randomno)
guesses = 0
userguess = None

while userguess != randomno:
    userguess = int(input("Enter Your Guess - "))
    if userguess == randomno:
        print("You guessed the correct number")
    else:
        if userguess > randomno:
           print("You guessed it wrong.. Enter a smaller Number")
        else:
            print("You guessed it worng ..Enter a higher number")
    guesses += 1

print(f"You guessed the number in {guesses} guesses")

with open('C:/Users/Sonit/Desktop/ZZ.PythoN/Part 10- Project 2/highscore.txt', 'r') as f:
    highscore = int(f.read())

if (guesses < highscore):
    print("yay!! You managed to break the highscore!!")
    with open('C:/Users/Sonit/Desktop/ZZ.PythoN/Part 10- Project 2/highscore.txt','w') as f:
        f.write(str(guesses))