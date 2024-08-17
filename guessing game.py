import random

# Prompt for range input
try:
    max_range = int(input("Please enter the range [Number]: "))
    if max_range <= 0:
        raise ValueError("Please enter an integer greater than 0.")
except ValueError as e:
    print(e)
    quit()

# Generate a random number within the specified range
random_number = random.randint(0, max_range)
guess_count = 0

# Start guessing loop
while True:
    guess_count += 1
    try:
        user_guess = int(input(f"Guess a number between 0 and {max_range}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess == random_number:
        print(f"You guessed the number! Congratulations!!")
        break
    elif user_guess < random_number:
        print("Your guess is low.")
    else:
        print("Your guess is high.")

print(f"You got it in {guess_count} guesses.")