import random
from time import sleep


def guessing_game():
    '''
      A Simple Guessing Game
    '''
    correct_num = random.randint(0, 100)

    while True:
        user_num = int(input("Please Guess a Number between 1 and 100: "))
        if not_valid_number(user_num):
            continue
        elif user_num > correct_num:
            print("Too High!")
        elif user_num < correct_num:
            print("Too Low!")
        elif user_num == correct_num:
            print("Just Right!")
            break


def not_valid_number(u_num):
    '''
      Helper function to check if the number is between
      1 and 100. 

      WARNING: No error checking
    '''
    if u_num not in range(1, 101):
        print('That was not a number between 1 and 100')
        sleep(1)
        return True


guessing_game()
