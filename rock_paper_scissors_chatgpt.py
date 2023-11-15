import random
# welcome in game
print("""welcome to 𝕣𝕠𝕔𝕜 𝕡𝕒𝕡𝕖𝕣 𝕤𝕔𝕚𝕤𝕤𝕠𝕣𝕤 𝕘𝕒𝕞𝕖""")
# confirm RUles
confirm = input("press(Enter or any key then Enter) to continue or type (help) for the rules :\n") .lower()
if confirm == "help" :
    print(
        """
        ****************** RULES ***************************
        1) YOu choose and the computer .
        2) Rock smashes scissors ----> Rock wins .
        3) Scissors cut paper  -----> scissors win .
        4) Paper covers rock -----------> paper wins.
        
        """
    )

# Initialize score counters
# Initialize score counters


user_score = 0
computer_score = 0

user_name = input("Enter your name player, it will be your name: ")

while not user_name:
    user_name = input("Please write your name: ")

print(f"Welcome, {user_name}!")


def play_game():
    global user_score, computer_score  # Declare score counters as global variables

    try:
        
        
        # Ask the user for their choice
        user = input(f"What's your choice {user_name}? 'r' for Rock, 'p' for Paper, and 's' for Scissors (or 'q' to quit)\n").lower()

        if user == 'q':
            print(f"Final Score - User: {user_score}, Computer: {computer_score}")
            return

        # Check if the user's input is valid
        if user not in ['r', 'p', 's']:
            print("Invalid input. Please enter 'r', 'p', or 's'.")
            play_game()
            return

        # Generate a random choice for the computer
        pc = random.choice(['r', 'p', 's'])
        
        # Define Unicode symbols for rock, paper, and scissors
        symbols = {'r': '🪨', 'p': '📄', 's': '✂️'}
        
        # Print out the choices with symbols
        print(f"{user_name}: {symbols[user]}")
        print(f"PC played: {symbols[pc]}")
        
        # Compare the choices to determine the winner
        if user == pc:
            print("It's a tie!")
        elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
            print("You won!")
            user_score += 1  # Update user's score
        else:
            print("You lose!")
            computer_score += 1  # Update computer's score

        # Display current score
        print(f"Current Score - {user_name}: {user_score}, Computer: {computer_score}")

        # Ask if user wants to play again
        replay = input("Do you want to play again? (y/n)\n")
        if replay.lower() == 'y':
            play_game()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        play_game()

# Call the function to start the game
play_game()
