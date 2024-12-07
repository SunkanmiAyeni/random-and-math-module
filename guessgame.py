import random
playing =True
number=str(random.randint(10,20))
print("I will generate a random number between 10 and 20 if you guess it correctly you win the game")
while playing:
    guess=input("enter your guess")
    if guess==number:
        print("Your guess is correct you win the game")
        break

    else:
        print("Your answer was wrong please try again")