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

# Gets the input of the user and assigns it to variable "guess"
guess = input('Enter a letter you would like to guess: ')

# Checks the user input is a single character
if len(guess) == 1:
    print('Good guess')
else:
    print('Oops! That is not a valid input.')

