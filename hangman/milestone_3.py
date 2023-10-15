import random

# list of words used for PC's word entry
word_list = ['strawberry', 'bananna', 'mango', 'watermelon', 'peach']

# Function to randomly choose from a list of words
def choice(words):
    rand = random.randint(0, 4)
    word_choice = words[rand]
    return word_choice

# Assigns the random word to the variable "word"
word = choice(word_list)
print(word)

def ask_for_input():
    # Gets the input of the user and assigns it to variable "guess"
    guess = input('\n\rEnter a letter you would like to guess: ')
    return guess

def check_guess(guess):
    # Checks the user input is a single alpha character
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Oops! That is not a valid input.')
    # Check if the letter is in "word" variable
    if guess in word:
        print(f'Good Guess! {guess} is in the word.')
    else:
        print(f'Wrong! {guess} is not in the word, try again.')

