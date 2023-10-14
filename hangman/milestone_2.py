import random

word_list = ['strawberry', 'bananna', 'mango', 'watermelon', 'peach']

def choice(words):
    rand = random.randint(0, 4)
    word_choice = words[rand]
    return word_choice

word = choice(word_list)

# print(word)

guess = input('Enter a letter you would like to guess: ')

if len(guess) == 1:
    print('Good guess')
else:
    print('Oops! That is not a valid input.')

