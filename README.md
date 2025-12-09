# Hangman (Python)

A simple console-based Hangman game written in Python.  
This was built as part of my Python learning journey using PyCharm

## 🎮 How the Game Works

- The game randomly selects a secret word from a word list.
- You have 6 lives to guess the word one letter at a time.
- Each wrong guess costs a life and updates the hangman ASCII art.
- If you reveal all the letters before your lives reach 0, you win.
- If your lives reach 0, you lose and the hidden word is revealed.

## 🧱 Project Structure

hangman.py        # Main game logic and loop
hangman_art.py    # ASCII logo and hangman stages
hangman_words.py  # List of possible secret words
