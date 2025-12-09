import random
import hangman_words
import hangman_art

#list of words to guess from hangman_word module
word_list = hangman_words.word_list
lives = 6

#from hangman_art module import the logo for menu
print(hangman_art.logo)

#choose a word from hangman_words module using random module
chosen_word = random.choice(word_list)

#creates a placeholder string and places underscores for the length of the word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#for the while loop, if the game_over is False the game keeps going if True it ends
#correct letters list store the correct letters guessed
game_over = False
correct_letters = []
incorrect_letters = []
#while loop
while not game_over:

    #prints how many lives the user has left and asks user for their guess letter
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    #display is an empty string to display the letters guessed correct

    display = ""
    #if the user guessed a letter already to not take a life and tell them the letter was already guessed
    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    if guess in incorrect_letters:
        print(f"You have already guessed {guess}, it was not in the word try again!")

    #if letter guessed is correct or in correct letters list display it, else add underscore for missing letters
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    #if guessed letter not in word tell the user and take a life and add incorrect letter to incorrect list
    #if guess in incorrect list do not take a life and tell to try again!

    if guess not in chosen_word and guess not in incorrect_letters:
        incorrect_letters.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that is not in the word and lost a life!")
        #if lives reach 0 the game is over and game_over is True to end while loop
        if lives == 0:
            game_over = True

            #displays the user lost and what the word was
            print(f"***********************YOU LOSE THE WORD WAS: {chosen_word}**********************")
    #if there are no more underscores in the display then all letters were guessed and the user won
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    #uses stages from hangman art module to display the hangman art and lives to enter the index corresponding to the
    #amount of lives
    print(hangman_art.stages[lives])
