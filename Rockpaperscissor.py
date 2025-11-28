import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif ((user == "rock" and computer == "scissors") or
          (user == "paper" and computer == "rock") or
          (user == "scissors" and computer == "paper")):
        return "User wins!"
    else:
        return "Computer wins!"
    
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules are: \n"
      "Rock vs Paper -- Paper wins."
      "Rock vs Scissor -- Rock wins."
      "Paper vs Scissor -- Scissor wins.")
    while True:
        user_choice = input("Enter rock, paper or scissors : ").lower().strip()

        if user_choice not in choices:
            print("Invalid choice! Please try again!")
            continue  # Skip the current loop and start a new one.

        computer_choice = random.choice(choices)
        print (f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no) : ").lower().strip()

        if play_again == "no":
            print("Thank you for playing!")
            break
play_game()
