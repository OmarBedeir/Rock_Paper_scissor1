# Start the game
# While Loop
#Try Block
#Ask the user for their choice
# Check if user wants to quit ('q')". If the user enters 'q', connect it to the "Break Loop" element
#Check if user input is valid ('r', 'p', 's')". If the input is invalid,  back to "User Input Prompt
#Generate a random choice for the computer
#Print User's Choice" and "Print PC's Choice
#Compare user and computer choices
#Display the result (Tie, Win, or Lose
#Except Block
# End of Loop
# End of Program




import random

while True:
    try:
        # Ask the user for their choice
        user = input("What's your choice? 'r' for Rock, 'p' for Paper, and 's' for Scissors (or 'q' to quit)\n").lower()

        if user == 'q':
            break

        # Check if the user's input is valid
        if user not in ['r', 'p', 's']:
            print("Invalid input. Please enter 'r', 'p', or 's'.")
            continue

        # Generate a random choice for the computer
        pc = random.choice(['r', 'p', 's'])

        # Print out the choices
        print("User played: " + user)
        print("PC played: " + pc)

        # Compare the choices to determine the winner
        if user == pc:
            print("It's a tie!")
        elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
            print("You won!")
        else:
            print("You lose!")

    except Exception as e:
        print(f"An error occurred: {e}")



