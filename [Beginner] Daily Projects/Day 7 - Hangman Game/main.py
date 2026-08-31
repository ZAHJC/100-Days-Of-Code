import random

# Imports resources that are contained in these files to allow clean code
import hangman_words
import hangman_art

# Gets wordlist from other file
word_list = hangman_words.word_list

# Sets lives
lives = 6

# Gets logo from other file
print(hangman_art.logo)

# Selects random word from word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Allows for placeholders to be printed to display a character amount for user
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Sets game state
game_over = False
# Collects letters user has guessed correctly
correct_letters = []

while not game_over:


    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"The letter {guess} has already been entered and is correct.")

    # Resets the display variable
    display = ""

    # Iterates through the chosen word, checks if guess is correct, adds to correct letters if so, and forms the string to print back
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Deals with failure state and losing of lives
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"The word was {chosen_word}")
            print(f"***********************YOU LOSE**********************")

    # Deals with win state
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(hangman_art.stages[lives])
