import random

class Hangman:
    def __init__(self, imported_words:list, num_lives):
        self.num_lives = num_lives
        self.imported_words = imported_words
        self.word = self.choice()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        self.list_of_avaliable_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']      
        
    # Function to randomly choose from a list of words
    def choice(self):
        rand = random.randint(0, len(self.imported_words) - 1)
        word_choice = self.imported_words[rand]
        word_choice_lower = word_choice.lower()
        return word_choice_lower

    # Gets the input of the user check it is valid and assigns it to variable "guess"
    def ask_for_input(self):
        word_guessed_string = ''.join(self.word_guessed)
        print(f'Can you guess what word I am thinking of? You get {self.num_lives} lives!')
        print(f'{word_guessed_string}')
        
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input('\n\rEnter a letter you would like to guess: ')

            # Checks the user input is a single alpha character
            if len(guess) != 1 or not guess.isalpha():
                print('Words usually have letters in. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You altready tried that letter!')        
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

            # Give a hint 
            if self.num_lives == 2 and self.num_letters >= 4 or self.num_lives == 1 and self.num_letters >= 3:
                need_a_hint = input('\n\rLooks liks you\'re struggling, need a hint? (y/n): ')
                if need_a_hint == 'y':
                    remaining_letters = set(self.list_of_avaliable_letters) - set(self.list_of_guesses)
                    missing_letter = remaining_letters.pop()
                    potential_hints = list(remaining_letters.intersection(set(self.word)))
                    missing_letter = random.choice(potential_hints)
                    print(f'Here\'s a hint: The word contains the letter "{missing_letter}".')
                else:
                    print('So you thint you\'re smart enough to beat me without hints?')

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
            print(''.join(self.word_guessed))
    
def play_game(imported_words):
    """
    Hangman Game

    This program is a command-line implementation of the Hangman game. The game randomly selects a word
    from a list of common words, and the player attempts to guess the word one letter at a time. The
    player has a limited number of lives to guess the word.

    Attributes:
        imported_words (list): A list of common words used for word selection.
        num_lives (int): The number of lives the player has to guess the word.

    Methods:
        choice: Randomly selects a word from the list of common words.
        ask_for_input: Gets input from the player, validates it, and checks if the letter is in the word.
        check_guess: Checks if the guessed letter is in the word and updates the word_guessed accordingly.
        play_game: Manages the gameplay, tracks lives, and determines the game's outcome.

    How to Play:
    - Enter a single letter at a time.
    - The game continues until you run out of lives or successfully guess the word.

    Have fun playing Hangman!
    """
    print('\n\rWelcome to hangman! To play the game, enter a single letter at a time.\n\r')
    num_lives = 6


    game = Hangman(imported_words, num_lives)

    # comment out to remove printed answer
    # print(game.word)

    # START GAME
    game.ask_for_input()

    if game.num_lives == 0:
        print('You lost!')
        print('''
 ___  _   _   ___  _  __ ___  ___   _   
/ __|| | | | / __|| |/ /| __|| _ \ | |  
\__ \| |_| || (__ |   < | _| |   / |_|  
|___/ \___/  \___||_|\_\|___||_|_\ (_)  
''')
        print(f'The word I was thinking of was "{game.word}".')
    else:
        print('Congratulations. You won the game!')
        print('''
                                 _       
                                | |      
  ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
| (_| (_) | | | | (_| | | | (_| | |_\__ \\
 \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                  __/ |                  
                 |___/                   
''')

    play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        play_game(imported_words)
    elif play_again == 'n':
        print('Ha! The computers will rise!')
    else:
        print('Maybe try reading the instructions next time.')

# Choosing the difficulty
while True:
    difficuly = input('Would you like me to go easy (e) or hard (h) on you? (e/h): ')
    if difficuly == 'e':
        from list_of_words import common_words_easy
        imported_words = common_words_easy
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif difficuly == 'h':
        from list_of_words import common_words_hard
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        imported_words = common_words_hard
        break
    else: 
        print('Type either "e" for easy or "h" for hard and press enter.')


play_game(imported_words)
