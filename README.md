# Hangman
Just a simple hangman program. This program utilizes the urllib library, as well as the random library. In addition, it uses the master hangman list from Xethron, which is linked here: https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt
A simple description of the code:
The code has a list with multi-line strings created in order to print the strings from the list easily. The code then selects a random word from that list. 
It proceeds to create an empty string called "underscores" that is used later with the hangman game. 
In the next line, a simple for loop appends the underscore to the empty underscore link, in order to show the player how many words there are. 
It then prints the underscores. 
Then, some variables are defined, such as guessnumber and guessnumberref, both of which were used in later lines of code. It then establishes a list that stores characters already guessed, so people don't guess the same letter over and over again. 
This is where the meat of the code starts, the while loop is basically just using the guess number to stop when it hits zero. This starts by setting a variable, underscores ref to be equal to underscores, which is important, because underscores is modified in the loop. 
A variable comes in that asks if the person thinks that they know the word. Based on the input, being y or n, it asks proceeding questions. 
Then the code does the standard hangman gameplay, as well as printing the corresponding string. 

Thank you to professorcool09 for the help!

I love fortnite battle pass and I am a pro fortnite player
