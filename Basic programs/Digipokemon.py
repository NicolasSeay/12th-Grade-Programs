import random

#class
class Critter(object):
    """A virtual pet"""
    def status(health, hunger, sleep, name, wins, losses):
        print "Health", health
        if health < 20:
            print name," is low on health!"
        print "Hunger", hunger
        if hunger < 20:
            print name, " is getting hungry!"
        print "Sleep", sleep
        if sleep >= 4:
            print name, " is getting sleepy!"
            
        print "\n", name," is still alive\n"
        print "Wins:", wins
        print "Losses:", losses
    status = staticmethod(status)

    def talk(self):
        print "Hi.  I'm", self.name, "\n"

#main
digipokemon = Critter()
name = raw_input("What will your Digipokemon's name be? ")
alive = True
health = 100
hunger = 50
sleep = 0
wins = 0
losses = 0
counter = 1
while alive == True:
    print "\nRound", counter
    print "---------------------------------"
    choice = raw_input("Sleep /  Eat / Battle / Status:  ")

    if choice == "sleep":
        health += 10
        hunger -= 10
        sleep = 0
    elif choice == "eat":
        sleep += 1
        randfood = random.randrange(1,5)
        print randfood
        if randfood == 0:
            #Yummy food  +10 health +10 hunger
            print "Yummy"
            health += 10
            hunger += 10
        elif randfood == 2 or randfood == 3 or randfood == 1 or randfood == 4:
            #Rations +15 hunger
            print "rations"
            hunger += 15
        elif randfood == 4:
            #Rotten -10 health, no change in hunger
            print "rotten"
            health -= 10
    elif choice == "battle":
        randbattle = random.randint(1,3)
        # 1 is a win
        # 2 is a loss
        if randbattle == 1:
            print "win"
            health += 10
            hunger -= 10
            wins += 1
            sleep += 1
        else:
            print "lose"
            health -= 10
            hunger -= 10
            losses += 1
            sleep += 1
    elif choice == "status":
        digipokemon.status(health, hunger, sleep, name, wins, losses)
        counter -= 1

    if sleep >= 5:
        health -= 10
        
    if health > 100:
        health = 100

    if wins == 10:
        print name, "has won!"
        alive = False
    elif health <= 0 or hunger >= 100 or hunger <= 0 or losses == 10:
        print "Health:", health
        print "Hunger:", hunger
        print name, " has died!"
        alive = False
    counter += 1
