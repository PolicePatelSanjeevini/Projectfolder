import random

def numberguessinggame():
    secretnumber = random.randint(1, 100)
    attempts = 10
    print("Welcome to guessing Number game!")
    print("Guess the number between 1 and 100.You have 10 attempts.")
    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}:Enter your guess: "))

        if guess < secretnumber:
            print("Too low!")
        elif guess > secretnumber:
            print("Too high!")
        else:
            print(f"Congratulations! you've guessed the correct number {secretnumber} in {i+1} attempts.")
    else:
        print(f"sorry you've used all {attempts} attempts.The correct number was {secretnumber}.")
if __name__ == "__main__":
    numberguessinggame()