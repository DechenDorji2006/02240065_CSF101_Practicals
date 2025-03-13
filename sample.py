import random

# Function for the Guess Number Game
def guess_number_game():
    print("\nWelcome to the Guess the Number Game!")
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    
    # Generate a random number within the given range
    number_to_guess = random.randint(lower_limit, upper_limit)
    
    # Set up a variable to keep track of the number of attempts
    attempts = 0
    
    while True:
        # Take user's guess as input
        guess = int(input(f"Guess a number between {lower_limit} and {upper_limit}: "))
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break
        
        # Ask the user if they want to continue or exit
        play_again = input("Do you want to keep guessing? (yes/no): ").lower()
        if play_again != 'yes':
            print("Returning to the main menu.")
            break

# Function for the Rock, Paper, Scissors Game
def rock_paper_scissors_game():
    print("\nWelcome to Rock, Paper, Scissors!")
    
    while True:
        # Get user's input
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please choose rock, paper, or scissors.")
            continue
        
        # Generate the computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
        else:
            print("Computer wins this round!")
        
        # Ask the user if they want to continue or exit
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Returning to the main menu.")
            break

# Main Menu Function
def main_menu():
    while True:
        print("\n==== Main Menu ====")
        print("1. Guess the Number Game")
        print("2. Rock, Paper, Scissors Game")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")

# Run the Main Menu
main_menu()
