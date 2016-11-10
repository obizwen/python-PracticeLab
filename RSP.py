'''
  The program should do the following:

    Prompt the user to select either Rock, Paper, or Scissors
    Instruct the computer to randomly select either Rock, Paper, or Scissors
    Compare the user's choice and the computer's choice
    Determine a winner (the user or the computer)
    Inform the user who the winner is
'''
from random import randint
from time import sleep

options = ["R", "P", "S"]
Loss_message = "You lost!"
Win_message = "You won!"

def decide_winner(user_choice, computer_choice):
    print "The user's choice is %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "The computer's choice is %s" % computer_choice
    user_choice_index = options.index(user_choice)
    choice_choice_index =  options.index(computer_choice)
    if user_choice == computer_choice:
        print "You draw a tie."
    elif user_choice == "R" and computer_choice == "S":
        print Win_message
    elif user_choice == "P" and computer_choice == "R":
        print Win_message
    elif user_choice == "S" and computer_choice == "P":
        print Win_message
    elif user_choice_index > 2:
        print "This is invalid option."
        return
    else:
        print Loss_message

def play_RPS():
    print "Playing RPS"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors")
    sleep(1)
    user_choice = user_choice.upper()
    #computer_choice = options[randint(0,2)]
    computer_choice = options[randint(0, len(options)-1)]
    decide_winner(user_choice, computer_choice)
    
play_RPS()