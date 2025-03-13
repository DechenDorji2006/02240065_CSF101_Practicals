import random

# First game: Guessing Number Game
def Guessing_number_game():
    print("Welcome to the guessing game!")
    running = True
    while running:
        num = random.randint(1, 100)
        guess_number = 0
        
        while guess_number != num:
            guess_number = int(input("Type your Guess: "))

            if (guess_number < num):
                print("Try again!")
            elif (guess_number > num):
                print("You can guess it next time!")
            else:
                print("You guessed the number! You Won!")

            # After each guess, ask if they want to continue or return to the menu
            play_again = input("Do you want to play once more or return to the menu? (y/n): ").lower()
            if not play_again == "y":
                running = False
                print("Returning to the main menu...")
                break

# Second game: Rock, Paper, Scissors
def Rock_paper_scissors_game():
    print("Welcome to the Rock Paper Scissors Game!")
    
    options = ("rock", "paper", "scissors")
    run = True
    while run:
        player = None
        while player not in options:
            player = input("Enter Your Option (rock, paper, scissors): ").lower()

        # Randomly generate the computer's choice
        computer_robot = random.choice(options)
        
        print(f"Player's choice: {player}")
        print(f"Computer's choice: {computer_robot}")

        if computer_robot == player:
            print("Tie Game!")
        elif player == "paper" and computer_robot == "rock":
            print("You won!")
        elif player == "scissors" and computer_robot == "paper":
            print("You won!")
        elif player == "rock" and computer_robot == "scissors":
            print("You won!")
        else:
            print("Computer won!")

        # Ask if the player wants to play again, even if they don't win
        play_again = input("Do you want to play once more? (y/n): ").lower()
        if not play_again == "y":
            run = False
            print("Returning to the main menu...")

# Main menu and the game loop
def main_menu_game():
    while True:
        print("\nGame Menu:\n1. Play Guess the Number Game\n2. Play Rock, Paper, Scissors Game\n3. Exit")
        option = input("Enter your choice: ")
        
        if option == '1':
            Guessing_number_game()
        elif option == '2':
            Rock_paper_scissors_game()
        elif option == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the menu
main_menu_game()
