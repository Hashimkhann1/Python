
# Guess Master game to guess the correct number.

import random

max_attempts = 3

user_guess = int(input("Inter Your Number from 1 to 9: ")) # Here I'm taking a number from the user to check with the random number
random_number = random.randint(1 , 9)    # # Here I'm generating a random number from 1 to 9

attempts = 0    # This variable used for 3 tries to guess the random number
print(random_number)
while(attempts < max_attempts):    # This while loop will repeat the process of entering the number for three times if the user does not guess the correct number

    if(user_guess == random_number):   # If the user guesses the correct number, this message will be displayed
        print("Congratulations! You win the game ******* :))")
        break
    elif(attempts == max_attempts - 1):
        print("You lose the game :(")   # If the user not guess the correct number for three times, this message will be displayed
    else:
        print("Not matched the number. Please try Again :(")    # When the number is not matched, this message will be displayed
        user_guess = int(input("Inter Your Number from 1 to 9: ")) # Taking the number again to check with the random number

    attempts += 1     # Incrementing the number by 1 to check for 3 tries in the while loop to finish the game.
