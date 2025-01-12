import random


def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    attempts = 0
    while True:
        # Take input from the player
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Check if the guess is correct
        if player_guess < number_to_guess:
            print("Too low! Try again.")
        elif player_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break


# Start the game
guessing_game()
