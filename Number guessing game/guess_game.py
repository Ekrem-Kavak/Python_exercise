# NUMBER GUESSING GAME: T
# The user guesses a number between 1 and 50. They will be successful if their guessed number are correct. There are a total of 5 rights in the game.  


import random

number = random.randint(1,50)

heart = 5

while heart > 0:    
    guess = int(input("Enter an integer between 1 and 50: "))
    heart -= 1
    if number == guess:
        print("Your guessed number is correct, congratulations. ")
        break 
    elif number < guess:
        print(f"Please enter a smaller number,your remaining right {heart}")
        continue
    elif number > guess:
        print(f"Please enter a larger number, your remaining right {heart}")
        continue
    else: 
        print("Enter a number in the desired number range")
   
print(f"True number is {number}")

