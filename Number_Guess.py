import random

secret_number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("I have chosen a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("\nCongratulations!")
            print("You guessed the number correctly.")
            print("Attempts Taken:", attempts)
            break

    except ValueError:
        print("Please enter a valid number!")

input("\nPress Enter to exit...")
