import random
number = random.randint(1,100)
guess = 0
print number
guess = raw_input("Guess: ")
while int(guess) != number:
    if int(guess) > number:
        print "Too high"
    elif int(guess) < number:
        print "Too low"
    guess = raw_input("Guess: ")
print "Correct!"
