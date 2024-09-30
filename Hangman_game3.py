import random

def choose_word():
    word_list = ["python", "hangman", "challenge", "random", "function", "developer", "software"]
    return random.choice(word_list).lower()

def display_word_state(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    wrong_letters = set()

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        current_state = display_word_state(word, guessed_letters)
        print(f"\nWord: {current_state}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters.union(wrong_letters)))}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_letters.add(guess)
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nYou've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
