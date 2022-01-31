import random
import time

# write a function(guessing_game) that takes no arguments


def guessing_game():
    '''
      A Simple Guessing Game
    '''
    # when run, the function chooses a random integer between 0 and 100(inclusive)
    correct_num = random.randint(0, 100)

    # Ask the user to guess what number has been chosen
    while True:
        user_guess = input("Please Guess a Number between 1 and 100: ")
        user_num = int(user_guess)
        if not_valid_number(user_num):
            continue
        # If higher print out "Too High"
        elif user_num > correct_num:
            print("Too High!")
        # If lower print out "Too Low"
        elif user_num < correct_num:
            print("Too Low!")
        # If correct print out "Just Right"
        elif user_num == correct_num:
            print("Just Right!")


def not_valid_number(u_num):
    '''
      Helper function to check if the number is between
      1 and 100. 

      WARNING: No error checking
    '''
    if u_num not in range(1, 101):
        print('That was not a number between 1 and 100')
        time.sleep(1)
        return True


guessing_game()
