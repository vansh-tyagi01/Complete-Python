import random

def Num_Guess_Game():
    random_number = random.randint(1,50)
    while(True):
        num = int(input("Enter a number :"))

        if num > 50 or num <= 0:
            print("Pls choose the number between 1 to 50")
        elif num > random_number:
            print("To High...")
        elif num < random_number:
            print("To Low...")
        else:
            print("Congratulation You Win👍")
            break

Num_Guess_Game()