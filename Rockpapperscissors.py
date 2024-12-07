import random
options =['rock',"paper","scissors"]
user=input("please enter rock,paper or scissors")
computer=random.choice(options)
print("You chose ",user)
print("computer chose",computer)
if user==computer:
    print("its a tie")
elif user=="rock" and computer=="scissors":
    print("You win the game")
elif user=="paper" and computer=="rock":
    print("You win the game")
elif user=="scissors" and computer=="paper":
    print("You win the game")
else:
    print("You lose the game")