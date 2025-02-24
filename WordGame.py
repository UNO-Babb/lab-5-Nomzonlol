#Word Game is a knock-off version of a popular online word-guessing game.
import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return letter == word[spot]

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    ratedWord = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            ratedWord += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            ratedWord += myGuess[i].lower()
        else:
            ratedWord += "*"
    return ratedWord


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    for guessNum in range(6):
        #Ask user for their guess
        myGuess = input("Guess a 5-letter word: ")

        #Give feedback using on their word:
        ratedGuess = rateGuess(myGuess, todayWord)
        print(ratedGuess)

        if myGuess == todayWord:
            print("You guessed it in", guessNum + 1, "tries!")
            return  # Exit the function if the word is guessed correctly

    print("You ran out of guesses. The word was:", todayWord)
