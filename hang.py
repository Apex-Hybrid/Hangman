import random
from words import words
import string


def get_word(words):
    word = random.choice(words)
    while '-' in words or '' in words:
        word = random.choice(words)
    return word.upper()


def hangman():
    lives = 5
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting a use input/letter
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'You have used {used_letters}, you have,{lives} lives left')

        # what current word is
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already used that letter. Go again')

        else:
            print('invalid')

    # gets here once len(word_letters) == 0 or lives == 0
    if lives == 0:
        print('Go back to shcool')
    else:
        print('You guessed', word, 'CORRECTLY!!!')


hangman()
