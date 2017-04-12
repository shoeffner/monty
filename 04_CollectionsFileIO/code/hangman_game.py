import random


ALLOWED_MISSES = 5
RULES = """
Hello! Let's play a game of hangman!
I already picked a word, and you now have to guess letters.
But be warned, if you guess more than {} times wrong, you lose!
""".format(ALLOWED_MISSES)


def read_possible_words(filename):
    with open(filename, 'r') as wordlist:
        return wordlist.read().splitlines()


def win(word):
    return '_' not in word


def loss(guesses):
    return ALLOWED_MISSES < len(guesses)


def initialize_word(wordlist):
    words = read_possible_words(wordlist)
    return random.choice(words)


def initialize_guess_word(word):
    guess_word = []
    for letter in word:
        guess_word.append('_')
    return guess_word


def print_state(guess_word, guessed_letters):
    print("Word: {} Wrong guesses: {}".format(guess_word, guessed_letters))


def update_guessword(guess_word, word, guessed_letter):
    """Updates the guess word.

    Places the guessed_letter at its positions in word into the guess_word,
    i.e.  if the guess_word was ['_', 'e', '_', '_', '_'], the word 'hello' and
    the guessed_letter 'l', the result would be ['_', 'e', 'l', 'l', '_'].

    This function modifies the list in place.

    Args:
    """
    for i, letter in enumerate(word):
        if letter == guessed_letter:
            guess_word[i] = letter
    return guess_word


def hangman():
    word = initialize_word('04_CollectionsFileIO/code/hangman_words.txt')
    guess_word = initialize_guess_word(word)

    print(RULES)

    guessed_letters = []
    while not win(guess_word) and not loss(guessed_letters):
        print_state(guess_word, guessed_letters)
        letter = input('Next guess? ')
        if letter in word:
            guess_word = update_guessword(guess_word, word, letter)
            if win(guess_word):
                print_state(guess_word, guessed_letters)
                print('You win! It was "{}".'.format(word))
        else:
            guessed_letters.append(letter)
    if loss(guessed_letters):
        print_state(guess_word, guessed_letters)
        print('Sorry, you lose. The word was "{}".'.format(word))


if __name__ == '__main__':
    hangman()
