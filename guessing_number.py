import random

def guessing_number_game():
    secret_number = random.randint(1, 10) # randinit(a, b) returns a random integer N such that a <= N <= b
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")

    chances = 3 

    while chances > 0:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        chances -= 1
    if chances == 0:
        print(f"Sorry, you've run out of chances. The secret number was {secret_number}.")

guessing_number_game()
