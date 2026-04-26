import random
print("welcomen to the game ,rps")
choices=("rock","paper","scissors")
computer=random.choice(choices)
user=input("enter your choice rock, paper, scissors")
print("computer choice is", computer)
if user==computer:
    print("this is a tie")
elif user=="rock":
    if computer=="scissors":
        print("user will win")
    else:
        print("computer will win")
elif user=="paper":
    if computer=="rock":
        print("user will win")
    else:
        print("computer will win")
elif user=="paper":
    if computer=="scissors":
        print("computer will win")
    else:
        print("user will win")
else:
    print("invalid choice")
