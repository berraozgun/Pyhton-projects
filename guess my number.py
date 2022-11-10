import random

secretNumber=random.randint(1,100)
guess = int(input("guess a number:"))
while (guess!=secretNumber):
    if (guess<secretNumber):
        print ("go up")
    if (guess>secretNumber):
        print ("go down")
        
    if (guess==secretNumber):
        print ("Congrats! You found the number!")
    else:
        print ("put valid number")

guess = int(input("guess a number:"))


