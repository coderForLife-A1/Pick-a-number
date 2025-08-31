import random

def display_menu():
    print("\n=== Number Guessing Game ===")
    print("1. Play Game")
    print("2. View High Score")
    print("3. Exit")

def get_user_choice():
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_user_guess():
    while True:
        guess = input("Enter your guess (1-100): ").strip()
        if guess.isdigit():
            guess_num = int(guess)
            if 1 <= guess_num <= 100:
                return guess_num
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Invalid input. Please enter a valid number.")

def play_game(high_score):
    number = random.randint(1, 100)
    attempts = 0
    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            if high_score is None or attempts < high_score:
                print("That's a new high score!")
                high_score = attempts
            break
    return high_score

def main():
    high_score = None
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            high_score = play_game(high_score)
        elif choice == '2':
            if high_score is None:
                print("\nNo games played yet. No high score available.")
            else:
                print(f"\nCurrent High Score: {high_score} attempts")
        else:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()