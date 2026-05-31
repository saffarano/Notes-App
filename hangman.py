import random

class Hangman():
    #Hangman class for playing hangman in client/server chat
    #initialized variables for the random word, no. of guesses, the progress
    #the player has made on the word, adn the letters they have guessed
    def __init__(self):
        self.randWord = None
        self.wrongGuess = 5
        self.guessWord = ''
        self.guessLetters = []

    def setWrongGuess(self, num):
        #if player gets a letter wrong, the count for guesses goes doun 1
        self.wrongGuess -= num

    def getWrongGuess(self):
        #get number of chances they have left
        return self.wrongGuess

    def getRandWord(self):
        #get the word to be guessed
        return self.randWord

    def getGuessWord(self):
        #get the progress on the word the player has made
        return self.guessWord

    def getGuessLetters(self):
        #get the list of letters the user has guessed
        return self.guessLetters

    def setGuessLetters(self, letter):
        #add a guessed letter to the list, sort alphabetically
        self.guessLetters.append(letter)
        self.guessLetters.sort()

    def gameStart(self):
        #initialize the game, open wordList text file and get as a list
        with open('wordList.txt', 'r') as infile:
            wordList = infile.readlines()

        #use the length and randInt to get a random index in the list,
        #set the word at that index to be the word the player will guess
        numWords = len(wordList)
        randIndex = random.randint(0, numWords - 1)
        #words have a blank space at the end, remove it
        self.randWord = wordList[randIndex].strip()

        for char in range(len(self.randWord)):
                self.guessWord += "_"

        return self.randWord, self.guessWord, self.wrongGuess, self.guessLetters

    # Takes a guessed letter from the user, compares to the unknown word and
    # Updates game parameters accordingly, Returns everything and status back
    # To Flask
    def playGame(self, letter, rand_word, guess_word, wrong_guesses, guess_letters):

        # make letter lowercase for consistency
        letter = letter.lower()

        # if a duplicate letter is guessed - return variables and status
        # indicator
        if letter in guess_letters:
            status = "Duplicate"
            return rand_word, guess_word, wrong_guesses, guess_letters, status

        # Multiple / Blank / Symbol entered: Send Invalid status
        elif len(letter) != 1 or not letter.isalpha():
            status = "Invalid"
            return rand_word, guess_word, wrong_guesses, guess_letters, status

        # Wrong Guess: Dec chances by 1, add letter to guessed letters
        elif letter not in rand_word:
            wrong_guesses -= 1
            guess_letters.append(letter)
            guess_letters.sort()
            # No chances left: Send Lose status
            if wrong_guesses == 0:
                status = "Lose"
                return rand_word, guess_word, wrong_guesses, guess_letters, status
            # Chances left: Indicate to continue game
            else:
                status = "Continue"
                return rand_word, guess_word, wrong_guesses, guess_letters, status

        # Correct Guess:
        else:
            # Build temp string by adding in guessed letter at right spot
            # Fill in from guess_word at remaining spots
            temp_str = ''
            for char in range(len(rand_word)):
                if letter == rand_word[char]:
                    temp_str += letter
                else:
                    temp_str += guess_word[char]

            # reassign the temp_str to the guess_word
            # add guessed letter to guesses
            guess_word = temp_str
            guess_letters.append(letter)
            guess_letters.sort()

            # Word Completed: return Win status
            if guess_word == rand_word:
                status = "Win"
                return rand_word, guess_word, wrong_guesses, guess_letters, status

            # Word incomplete: return Continue status
            else:
                status = "Continue"
                return rand_word, guess_word, wrong_guesses, guess_letters, status
