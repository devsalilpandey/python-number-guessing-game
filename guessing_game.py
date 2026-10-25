import random
secret_number = random.randint(1, 100)
attempts = 0
print("Welcome to the Guessing Game!")
while True:
    guess = input("Please enter your guess (between 1 and 100): ")
    
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please try again.")
            continue
    except ValueError:
        attempts += 1
        print("Invalid input. Please enter a number between 1 and 100.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
        break