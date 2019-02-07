class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "T", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]


    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(Card):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def dealForPlayer(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print "Can't continue deal. Out of cards!"
                    #repopulate deck
    def dealForDealer(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    top_card.flip()
                    self.give(top_card, hand)
                else:
                    print "Can't continue deal. Out of cards!"
                    #repopulate deck


def playOptions(hand):      #prints the available moves for the player
    print "\nHit(h)"
    print "Stand(s)"
    #if card1 is the same as card2 --> Split
    if rounds == 1:
        #if enough money
        print "Double(d)"
        print "Surrender(su)"

def getRankOfCard(self):    #returns the string value of the cards rank
    return self.rank

def getValueOfHand(self):   #returns total value of ranks in the hand
    nums = []
    for c in self.cards:
        if c.rank == '2' or c.rank == '3' or c.rank == '4' or c.rank == '5' or c.rank == '6' or c.rank == '7' or c.rank == '8' or c.rank == '9':
            nums.append(int(c.rank))
        elif c.rank == "T" or c.rank == "J" or c.rank == "Q" or c.rank == "K":
            nums.append(10)
        elif c.rank == "A":
            nums.append(11)
    
    final = sum(nums)
    while final > 21 and nums.count(11):
        nums[nums.index(11)] = 1
        final = sum(nums)
        
    return final

#main
playagain = True
gamestillplaying = True
money = 100

deck1 = Deck()      #created
#deck1.populate()    #populated
#deck1.shuffle()     #shuffled

deck1.add(Card("9", "s"))      #Even Money
deck1.add(Card("Q", "s"))
deck1.add(Card("J", "d"))
deck1.add(Card("A", "s"))

#deck1.add(Card("7", "s"))      #Insurance
#deck1.add(Card("8", "s"))
#deck1.add(Card("A", "s"))
#deck1.add(Card("Q", "s"))

#deck1.add(Card("Q", "s"))      #Split
#deck1.add(Card("Q", "s"))
#deck1.add(Card("Q", "s"))
#deck1.add(Card("8", "s"))

#deck1.add(Card("A", "s"))      #Ace Split
#deck1.add(Card("A", "d"))
#deck1.add(Card("T", "s"))
#deck1.add(Card("8", "s"))

#deck1.add(Card("8", "s"))       #double down
#deck1.add(Card("8", "d"))
#deck1.add(Card("8", "c"))
#deck1.add(Card("9", "s"))
#deck1.add(Card("5", "h"))

#deck1.add(Card("A", "s"))      #Natural Blackjack
#deck1.add(Card("Q", "s"))
#deck1.add(Card("9", "d"))
#deck1.add(Card("8", "s"))

    
while playagain == True:    #loop for each round
    print "-----------------------------"
    rounds = 1
    doIFlip = True
    playerturn = True
    playagain = True
    gamestillplaying = True
    bust = False
    
    
    
    
    dealer_hand = Hand()
    player_hand = Hand()
    phand = [player_hand]
    dhand = [dealer_hand]
    deck1.dealForPlayer(phand, per_hand = 2)
    deck1.dealForPlayer(dhand, per_hand = 1)
    deck1.dealForDealer(dhand, per_hand = 1)
    player = Player(player_hand)
    print "You currently have $", money
    bet = raw_input("What amount do you want to bet? ")
    if int(money) - int(bet) < 0:     #Checking to see if the player has enough money to make the bet
        print "You don't have enough money to do that!"
        bet = raw_input("What amount do you want to bet? ")
    
    while gamestillplaying == True:     #loop for each decision

        if getRankOfCard(dealer_hand.cards[0]) == "A" and rounds == 1:
            print "Dealer's hand:", dealer_hand
            print "\nPlayer's hand:", player_hand
            print "Player showing:", getValueOfHand(player_hand)
            print ""
            if getValueOfHand(player_hand) == 21:   #Even Money
                evenmoney = raw_input("Even Money? (y/n): ")
                if evenmoney == "y":
                    if getValueOfHand(dealer_hand) == 21:   #if Dealer has blackjack
                        playerturn = False
                        gamestillplaying = False
                        money += int(bet)
                    else:   #if Dealer does NOT have blackjack
                        playerturn = False
                        gamestillplaying = False
                        money -= int(bet)
                else:
                    playerturn = False
                    gamestillplaying = False
                        
            else:   #Insurance
                insurance = raw_input("How much do you want to insure? ")
                if getValueOfHand(dealer_hand) == 21:
                    money += int(insurance)
                    playerturn = False
                    gamestillplaying = False
                else:
                    
                    money -= int(insurance)
                
                
        elif rounds == 1 and getValueOfHand(player_hand) == 21 and getValueOfHand(dealer_hand) != 21:     #if Player has Natural Blackjack
            gamestillplaying = False
            money += int(bet)*.5
            
        elif rounds == 1 and getValueOfHand(player_hand) != 21 and getValueOfHand(dealer_hand) == 21:   #if Dealer has Natural Blackjack
            playerturn = False
            gamestillplaying = False
            money -= int(bet)*.5

        if playerturn == True:
            print "Dealer's hand:", dealer_hand
            print "\nPlayer's hand:", player_hand
            print "Player showing:", getValueOfHand(player_hand)
            print ""
            
            if rounds == 1 and getValueOfHand(player_hand) == 21:   #CHECKS FOR NATURAL BLACKJACK
                if getRankOfCard(dealer_hand.cards[0]) == "A":
                    evenmoney = raw_input("Even money? (y/n) ")

            playOptions(player_hand)
            if rounds == 1:
                if getRankOfCard(player_hand.cards[0]) == getRankOfCard(player_hand.cards[1]) and (int(money) - 2*int(bet) >= 0):
                    print "Split(sp)"
            
            option = raw_input("\nMake your move: ")
            print ""
            if option == "h":   #HIT
                
                deck1.dealForPlayer(phand, per_hand = 1)
                if getValueOfHand(player_hand) > 21:
                    print "Dealer's hand:", dealer_hand
                    print "\nPlayer's hand:", player_hand
                    print "Player showing:", getValueOfHand(player_hand)
                    print ""
                    print "You have busted!"
                    bust = True
                    gamestillplaying = False
            elif option == "s": #STAND
                playerturn = False
            elif (option == "d" and (money - 2*int(bet) >= 0)): #DOUBLE
                bet = float(bet) + float(bet)
                playerturn = False
                #DOUBLE THE BET
                deck1.dealForPlayer(phand, per_hand = 1)
                if getValueOfHand(player_hand) > 21:
                    print "Dealer's hand:", dealer_hand
                    print "\nPlayer's hand:", player_hand
                    print "Player showing:", getValueOfHand(player_hand)
                    print ""
                    print "You have busted!"
                    bust = True
                    gamestillplaying = False
            elif option == "su":    #SURRENDER
                print "You have surrendered!"
                money += int(bet)*.5
                bust = True
                playerturn = False
                gamestillplaying = False
            elif option == "sp":    #SPLIT
                split_hand = Hand()
                shand = [split_hand]
                player_hand.give(player_hand.cards[1], split_hand)
                deck1.populate()
                deck1.shuffle()
                if getRankOfCard(player_hand.cards[0]) == "A":
                    playerturn = False
                    deck1.dealForPlayer(phand, per_hand = 1)
                    deck1.dealForPlayer(shand, per_hand = 1)
                    print "Split hand:", split_hand
                    print "Split hand showing:", getValueOfHand(split_hand)
                    print ""
                    if getValueOfHand(split_hand) > getValueOfHand(dealer_hand):
                        money += int(bet)
                    elif getValueOfHand(split_hand) < getValueOfHand(dealer_hand):
                        money -= int(bet)
            else:
                print "That is not an option"

        else:
            if doIFlip == True:
                dealer_hand.cards[1].flip()
                doIFlip = False
            print "Dealer's hand:", dealer_hand
            print "Dealer showing:", getValueOfHand(dealer_hand)
            
            print "\nPlayer's hand:", player_hand
            print "Player showing:", getValueOfHand(player_hand)
            print ""
            if getValueOfHand(dealer_hand) >= 17:
                gamestillplaying = False
                if getValueOfHand(dealer_hand) > 21:
                    print "Dealer's hand:", dealer_hand
                    print "Dealer showing:", getValueOfHand(dealer_hand)
                    
                    print "\nPlayer's hand:", player_hand
                    print "Player showing:", getValueOfHand(player_hand)
                    print ""
                    print "The dealer has busted!"
                    bust = True
                    gamestillplaying = False
            else:
                deck1.dealForPlayer(dhand, per_hand = 1)
                if getValueOfHand(dealer_hand) > 21:
                    print "Dealer's hand:", dealer_hand
                    print "Dealer showing:", getValueOfHand(dealer_hand)
                    
                    print "\nPlayer's hand:", player_hand
                    print "Player showing:", getValueOfHand(player_hand)
                    print ""
                    print "The dealer has busted!"
                    bust = True
                    gamestillplaying = False
        rounds += 1
    if (getValueOfHand(player_hand) > getValueOfHand(dealer_hand)) and bust == False:   #if player > dealer
        print "You have won this round"
        money += int(bet)
    elif (getValueOfHand(player_hand) < getValueOfHand(dealer_hand)) and bust == False: #if player < dealer
        print "You have lost this round"
        money -= int(bet)
    elif (getValueOfHand(player_hand) == getValueOfHand(dealer_hand)) and bust == False: #if equal
        print "It is a tie"
    if bust == True:
        money -= int(bet)
    print "You now have $", money

    #checking if player has enough money to keep playing, if not, ends the game
    if money <= 0:
        playagain = False

    deck1.populate()
    deck1.shuffle()

#after the game has ended
print "You have lost!"
