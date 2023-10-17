import random

class Hangman:
    def __init__(self, word_list:list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = self.choice()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []      
        
    # Function to randomly choose from a list of words
    def choice(self):
        rand = random.randint(0, len(self.word_list) - 1)
        word_choice = self.word_list[rand]
        return word_choice

    # Gets the input of the user and assigns it to variable "guess"
    def ask_for_input(self):
        word_guessed_string = ''.join(self.word_guessed)
        print(f'Can you guess what word I am thinking of? You get {self.num_lives} lives!')
        print(f'{word_guessed_string} which has {self.num_letters} letters.')
        while True:
            guess = input('\n\rEnter a letter you would like to guess: ')
            # Checks the user input is a single alpha character
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You altready tried that letter!')        
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def check_guess(self, guess):
        # Change guess to lower case
        guess_lower = guess.lower()
        # Check if the letter is in "word" variable
        if guess_lower in self.word:
            print(f'Good Guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if guess_lower == letter:
                    self.word_guessed[index] = guess_lower
                    self.num_letters -= 1
            print(''.join(self.word_guessed))
        else:
            print(f'Wrong! {guess} is not in the word, try again.')
            self.num_lives -= 1
            print(f'You now have {self.num_lives} lives.')


# list of words used for PC's word entry
word_list = ['st', 'ba', 'mao', 'walon', 'peh']

def play_game(word_list):
    num_lives = 5
    while True:
        game = Hangman(word_list, num_lives)
        print(game.word)

        while num_lives > 0 and game.num_letters > 0:
            game.ask_for_input()

        if num_lives == 0:
            print('You lost!')
        else:
            print('Congratulations. You won the game!')

        play_again = input('Would you like to play again? (y/n)')
        if play_again == 'y':
            play_game(word_list)
        elif play_again == 'n':
            print('Ha! The computers will rise!')
            break
        else:
            print('Maybe try reading the instructions next time.')
            break

play_game(word_list)
