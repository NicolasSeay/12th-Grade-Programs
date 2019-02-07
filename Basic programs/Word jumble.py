import random
counter = 0
numcorrect = 0;
wordbank = ("starwars", "vader", "anakin", "lightsaber", "deathstar")
while (numcorrect != 3):
    wordpos = random.randint(0, len(wordbank))
    word = wordbank[wordpos]
    original = word
    newword = ""
    wordbank = wordbank[:wordpos] + wordbank[wordpos+1:]
    #print wordbank
    for letter in word:
        position = random.randint(0, len(word)-1)
        #print position
        newword += word[position]
        word = word[:position] + word[position+1:]
        #print word
        #print newword
        #print ""
    print
    guess = 0
    while guess != original:
        counter += 1
        guess = raw_input("Guess: ")
    numcorrect += 1

print "Correct! Completed in " + str(counter) + " guesses."
