import random
print("welcome to the game")
computer=random.randint(1,10)
user=int(input("enter a number between 1 to 10"))
if user==computer:
    print("you won the game")
else:
    print('you lost the game')
    print('the real number is ', computer)