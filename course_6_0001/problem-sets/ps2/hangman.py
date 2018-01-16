# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Cast secret_word to a list and then a set to create a collection of 
    # unique letters to iterate through and return False if any letter is not
    # in letters_guessed, otherwise returns True
    for letter in set(list(secret_word)):
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Initialize guess_word then iterate through secret_word to find blanks
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # Initialize available_letters then iterate through letters_guessed and
    # remove them from available_letters
    available_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        available_letters.remove(letter)
    # Join the list of available_letters with a blank space to return a string
    # of available letters
    return ''.join(available_letters)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Show welcome message and word length
    print('Welcome to the game hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    # Loop until word is guessed
    while not is_word_guessed(secret_word, letters_guessed):
        # Print status
        print('-------------')
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # Set guessed_letter to lowercase from user input
        guessed_letter = input('Please guess a letter: ').lower()
        # Check that guessed_letter is valid and not already guessed
        if guessed_letter in string.ascii_lowercase and guessed_letter not in letters_guessed:
            # Add to letters_guessed
            letters_guessed += guessed_letter
            # Setting guessed_word variable looks prettier
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            # Check that guessed letter is in secret_word
            if guessed_letter in secret_word:
                print('Good guess:', guessed_word)
            else:
                print('Oops! That letter is not in my word:', guessed_word)
                # Determine how many guesses to deduct
                if guessed_letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
        else:
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            # Set rule message
            if guessed_letter not in string.ascii_lowercase:
                rule = 'That is not a valid letter.'
            elif guessed_letter in letters_guessed:
                rule = 'You\'ve already guessed that letter.'
            # Check if there are any warnings to deduct, otherwise deduct guesses
            if warnings > 0:
                warnings -= 1
                print('Oops!', rule, 'You have', warnings, 'warnings left:', guessed_word)
            else:
                guesses -= 1
                print('Oops!', rule, 'You have no warnings left so you lose one guess:', guessed_word)
        # Print game over message and return
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            return
    # Set score and print win message
    score = guesses * len(set(secret_word))
    print('Congratulations, you won!')
    print('Your total score for this game is:', score)
      

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # Cast both words to a list containing their letters in order
    # Replace spaces in my_word with blanks for length comparison
    my_word_letters = list(my_word.replace(' ',''))
    other_word_letters = list(other_word)
    # If length isn't equal then return False
    if len(my_word_letters) == len(other_word_letters):
        # Loop through range equal to length of my_word_letters and use the loop variable
        # i to compare indices
        for i in range(len(my_word_letters)):
            # Continue if letter at index i is equal
            if my_word_letters[i] == other_word_letters[i]:
                continue
            # Continue if letter is _ and the current letter at index i in other_word_letters
            # isn't already in my_word_letters
            elif my_word_letters[i] == '_' and other_word_letters[i] not in my_word_letters:
                continue
            else:
                return False
        return True
    else:
        return False         


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches += word + ' '
    if possible_matches != '':
        print(possible_matches)
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
       # Show welcome message and word length
    print('Welcome to the game hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    # Loop until word is guessed
    while not is_word_guessed(secret_word, letters_guessed):
        # Print status
        print('-------------')
        print('You have', guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        # Set guessed_letter to lowercase from user input
        guessed_letter = input('Please guess a letter: ').lower()
        # Show hints
        if guessed_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        # Check that guessed_letter is valid and not already guessed
        elif guessed_letter in string.ascii_lowercase and guessed_letter not in letters_guessed:
            # Add to letters_guessed
            letters_guessed += guessed_letter
            # Setting guessed_word variable looks prettier
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            # Check that guessed letter is in secret_word
            if guessed_letter in secret_word:
                print('Good guess:', guessed_word)
            else:
                print('Oops! That letter is not in my word:', guessed_word)
                # Determine how many guesses to deduct
                if guessed_letter in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
        else:
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            # Set rule message
            if guessed_letter not in string.ascii_lowercase:
                rule = 'That is not a valid letter.'
            elif guessed_letter in letters_guessed:
                rule = 'You\'ve already guessed that letter.'
            # Check if there are any warnings to deduct, otherwise deduct guesses
            if warnings > 0:
                warnings -= 1
                print('Oops!', rule, 'You have', warnings, 'warnings left:', guessed_word)
            else:
                guesses -= 1
                print('Oops!', rule, 'You have no warnings left so you lose one guess:', guessed_word)
        # Print game over message and return
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            return
    # Set score and print win message
    score = guesses * len(set(secret_word))
    print('Congratulations, you won!')
    print('Your total score for this game is:', score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
