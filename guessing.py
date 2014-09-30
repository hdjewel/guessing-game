import random

# get the player's name from the user
username = raw_input("Please enter your name: ")
# print the greeting
print ("Hello guessing game player %s.  It's nice to meet you.") % username

# generate a random number for the player to guess
random_number =  random.randrange(1,101)



