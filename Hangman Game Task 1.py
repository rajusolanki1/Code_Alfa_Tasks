import random

words = ["apple", "tiger", "house", "chair", "water"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("=== Welcome to Hangman ===")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")
        print("Guesses left:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)
