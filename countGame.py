import random
number=random.randint(1,9)
chance=0

while chance<5:
    guess=int(input("Enter your guess between 1 and 9:"))
    if guess==number:
        print("You are right")
elif guess<number:
        print("Your guess too low guess a number higher")
else:
        print("Your guess too high guess a number lower")
    chance=chance+1

if not chance<5:
    print( "You lose,The number is",number )