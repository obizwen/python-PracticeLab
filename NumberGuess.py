'''
	Dice game.
  '''
from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(raw_input("Enter the guess: "))
    return user_guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = 2*number_of_sides
    print "Max possible value: %s" % max_val
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "Guess invalid"
        return
    else:
      	print "Rolling..."
        sleep(2)
        print "First roll: %d" % first_roll
        sleep(1)
        print "Second roll: %d" % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "Total roll: %d" % total_roll
        print "Result..."
        sleep(1)
        if user_guess > total_roll:
            print "Congrats, you won!"
            return
        else:
            print "Sorry, you lose."
            return
roll_dice(6)