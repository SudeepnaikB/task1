import random
import time

number = random.randint(1, 200)  # pick the number between 1 and 200

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(name):
    guessesTaken = 0
    while guessesTaken < 6:  # if the number of guesses is less than 6
        time.sleep(0.25)
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string    

            if 1 <= guess <= 200:  # if they are in range
                guessesTaken += 1  # adds one guess each time the player is wrong
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break  # if the guess is right, then we are going to jump out of the while block
            else:  # if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:  # if a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")
            
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    else:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    name = intro()
    pick(name)
    print("Do you want to play again?")
    playagain = input()
