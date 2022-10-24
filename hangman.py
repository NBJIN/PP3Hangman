import random
from words import words

print("\nWelcome to the Hangman Game!")
name = input("What is your name: ")
print("Best of Luck " + name)
print("The game will start shortly...")


def get(words):
    words = random.choice("words")
    return words.upper()


def play(words):
    words = get(words)
    player_lives = 6
    letters_guessed = []
    words_guessed = []

    while letters_guessed and player_lives > 0:
        player_lives = input("Guess a letter")
