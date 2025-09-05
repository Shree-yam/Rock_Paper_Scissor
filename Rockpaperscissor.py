import random

print("Rules are: \n"
      "Rock vs Paper -- Paper wins."
      "Rock vs Scissor -- Rock wins."
      "Paper vs Scissor -- Scissor wins.")

while True:
    print("Enter your choice, Rock, Paper or Scissors:")
    choice = input("Enter your choice: ").capitalize()

    while choice not in ("Rock", "Paper", "Scissors"):
        print("Invalid choice. Please choose Rock, Paper or Scissors.")
        choice = input("Enter your choice: ").capitalize()

        print("You chose:", choice)
        print("Now it's the computers turn...")

        comp_choice_num = random.randint(1, 3)
        if comp_choice_num == 1:
            comp_choice = "Rock"
        elif comp_choice_num == 2:
            comp_choice = "Paper"
        elif comp_choice_num == 3:
            comp_choice = "Scissors"

        print("Computer chose:", comp_choice)

        # Checking draw

        if choice == comp_choice:
            print("It's a draw...")
        else:

            # Determining the winner

            if choice == "Rock":
                if comp_choice == "Paper":
                    print("Paper wins...")
            else:
                print("Rock wins ...")
            elif choice == "Paper":
                print("It's a draw...")
            if comp_choice == "Scissor":
                    print("Scissor wins ...")
            else:
                print("Paper wins ...")
            elif choice == "Scissor":
                         
            if comp_choice == "Rock":
                print("Rock wins ...")
            else:
                print("Scissor wins ...")
