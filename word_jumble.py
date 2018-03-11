#Word Jumble

import random

#import a sequence of words to choos from
WORDS = ("words_common.txt")

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print ("Loading word list from file...)"
    # inFile: file
    inFile = open(WORDS, 'r')
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist
    
wordlist = load_words()
word = random.choice(wordlist)

#Create a variable to see if the guess is correct
correct = word

#create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]


#start the game
print(
    '''
                    Welcome to Word Jumble!
        Unscramble the letters to make a word.
        (Press the enter key at the prompt to quit.)

    '''
    )

print ("The jumble is:", jumble)

tries = 0
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess= input("Your guess: ")   


if guess == correct:
    print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
exit ()
