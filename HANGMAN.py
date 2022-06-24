## Setting up the libraries and such
import urllib.request
import random
word_site = "https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt"
response = urllib.request.urlopen(word_site)
long_txt = response.read().decode()
words = long_txt.splitlines()

def hangman():
    stringlist = ["______  \n|    |  \n|       \n|      \n|       \n|       \n⊥       ", "______  \n|    |  \n|    O  \n|      \n|       \n|       \n⊥       ", "______  \n|    |  \n|    O  \n|    | \n|    |  \n|       \n⊥       ", "______  \n|    |  \n|    O  \n|   \| \n|    |  \n|       \n⊥       ", "______  \n|    |  \n|    O  \n|   \|/\n|    |  \n|       \n⊥       ", "______  \n|    |  \n|    O  \n|   \|/\n|    |  \n|  ./   \n⊥       ", "______  \n|    |  \n|    O  \n|   \|/\n|    |  \n|  ./ \.\n⊥       "]
    wordtoguess = random.choice(words)
    underscores = ""
    print(stringlist[0])
    for i in range(len(wordtoguess)):
        underscores += "_"
    print(underscores)
    guessnumber = 6
    guessnumberref = 0
    charactersguessedincorrect = []
    while guessnumber > 0:
        underscoresref = underscores
        inputifknowword = input("Type y if you think you know the word, and n if you want to keep guessing individual letters! ").lower()
        if inputifknowword == 'y':
            guesstheword = input(" \nType the word that you think it is! ").lower()
            if guesstheword == wordtoguess:
                print("EZ VICTORY ROYALE")
                break
            else:
                guessnumber -= 1
                print("You have " + str(guessnumber) + " guesses left!")
                guessnumberref += 1
                print(stringlist[guessnumberref])
        elif inputifknowword == 'n': 
            inputcharacter = input("Please input a letter: ").lower()
            while len(inputcharacter) > 1:
                print('bro that\'s not a character, you good?' )
                inputcharacter = input("Please input a letter: ").lower()
            if inputcharacter in charactersguessedincorrect:
                print("You already guessed that bruh. ")
            for i in range(len(wordtoguess)):
                if inputcharacter == wordtoguess[i]:
                    underscores = underscores[:i] + inputcharacter + underscores[i+1:]
            
            if underscoresref == underscores and inputcharacter not in charactersguessedincorrect:
                
                guessnumber -= 1
                print("You have " + str(guessnumber) + " guesses left!")
                guessnumberref += 1
                print(stringlist[guessnumberref])
            if underscoresref != underscores:
                print("Good job, you got a match! ")
                print(stringlist[guessnumberref])
            charactersguessedincorrect.append(inputcharacter)
            print(underscores)
            if underscores == wordtoguess:
                print("EZ VICTORY ROYALE")
                break
        else:
            print('learn how to type bozo. ')
    if guessnumber == 0:
        print("You lost L bozo. The word was " + wordtoguess + ", get good loser.")
               
hangman()





nice = '69'