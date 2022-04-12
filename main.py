# Imports
from hangmanart import HANGMANPICS
import time
# Opening the word that must be guessed
f = open("hangman", "r")
hangmanword = (f.read())
f.close()
# Creating a list of the letters in the word
letterlist = list(hangmanword)
# Lists
Guessd_Letters = ["Your guessed incorrect letters are: "]
displaylist = []
# Adding the correct number of _ which show letter places to the list
for i in letterlist:
    displaylist.append("_")
# This is the code for adding spaces into the code if the word is a phrase
spacecharechter = " "
# locates all the spaces
spaces = [i for i in range(len(letterlist)) if letterlist[i] == spacecharechter]
space = 0
while True:
    # THis prints all of the spaces out
    if space < len(spaces):
        displaylist.pop((spaces[space]))
        displaylist.insert((spaces[space]), spacecharechter)
        space = space + 1
    # Code for when all the locations of the space have been printed
    else:
        break
# Printing the list
print("This is the word:\n")
print(*displaylist)
# Printing the noose
print(HANGMANPICS[0])
# Setting counter = to 0
counter = 0
time.sleep(2)
while True:
    # Printing the list of guessed letters
    time.sleep(1)
    print(*Guessd_Letters)
    print("The word is:")
    print(*displaylist)
    guess = input("Please enter a letter or word: ")
    # Detecting if you lost or not
    if counter == 5:
        print(HANGMANPICS[6])
        time.sleep(1)
        print("You did not get the word. You suck. Get a life\n")
        time.sleep(1)
        print("The word was " + hangmanword)
        exit()
    # Detecting if you got the correct word
    elif guess == hangmanword:
        print("You got the word. Congrats\n")
        time.sleep(1)
        print("The word was " + hangmanword)
        exit()
    # Detecting if the letter is in the word
    elif letterlist.count(guess) == 0:
        print("That is not a letter or the word.")
        Guessd_Letters.append(guess)
        Artlocation = counter + 1
        print(HANGMANPICS[Artlocation])
        # Counter is the number of incorrect guesses
        counter = counter + 1
    else:
        # locount is used to detect if there is multiple letters in the statment and to print them all.
        locount = 0
        # THis gives you the location of all the appearances of the letter
        locations = [i for i in range(len(letterlist)) if letterlist[i] == guess]
        while True:
            # If there is more locations of the letter than printed this code will keep printing
            if locount < len(locations):
                displaylist.pop((locations[locount]))
                displaylist.insert((locations[locount]), guess)
                locount = locount + 1
            # Detecting if you got the word
            elif displaylist.count("_") == 0:
                print("You got the word. Congrats\n")
                time.sleep(1)
                print("The word was " + hangmanword)
                counter = 0
                exit()
            # Code for when all the locations of the letters have been printed
            else:
                break
        print(*displaylist)