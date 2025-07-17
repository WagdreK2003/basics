# create guess a number game where the user will enter a number and the computer will generate a random number and the user will give an input and you need to tell him wheether the number is correct or not. if the number is less or more, let him know so he can guess the number accordingly. use random library.
import random
num = random.randint(1, 10)
no= int(input("Enter a number between 1 and 10: "))
if no == num:
    print("right guess")
elif no < num:
    print("your guess is less than the number")
else:
    print("your guess is more than the number")
print("The number is", num)