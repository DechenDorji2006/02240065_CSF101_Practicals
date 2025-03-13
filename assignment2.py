import random

#first game
def Guessing_number_game():
    print("Welcome to the guessing game!")
    #running = True
    #while running == True:
    num = random.randint(1,100)
    guess_number = 0
        
    while guess_number != num:
        guess_number = int(input("Type your Guess from 1 to 100"))

        if (guess_number < num):
            print("Try again")
        elif (guess_number > num):
            print("You can guess it next time")
        else:
            print("You guessed the number, You Won!")

        play_again = input("Do you wanna play once more,(y/n)").lower()
        if not play_again == "y":
        #running = False
            print("Thanking you for playing, Returning to menu...")
            break
    
    #print("Thank you for playing")
            

#second game
def Rock_paper_scissors_game():
    print("Welcome to the Rock Paper Scissors Game")

    options = ("rock", "paper", "scissors")
    #run = True 
    #while run == True:
    player = None
    while player not in options:
        player = input("Enter Your Option(rock,paper,scissor)")

        computer_robot = random.choice(options)

        print(f"player chioce:{player}")
        print(f"computer chioce:{computer_robot}")

        if computer_robot == player:
            print("Tie Game")
        elif player == "paper" and computer_robot == "rock":
            print("You won!")
        elif player == "scissors" and computer_robot == "paper":
            print("You Won")
        elif player == "rock" and computer_robot == "scissors":
            print("You won!")
        else:
            print("Computer won!")

        play_again = input("Do you wanna play once more,(y/n)").lower()
        if not play_again == "y":
            #run = False
            print("Thanking you for playing, Returing to menu...")
    

#for menu
def main_menu_game():
    while True:
        print("\nGame Menu:","\n1.Play Guess the Number Game","\n2. Play Rock, Paper, Scissors Game","3. Exit")
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

main_menu_game()

