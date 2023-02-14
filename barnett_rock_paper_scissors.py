# Rock, Paper, Scissors game
import random  # This module imports the Python code for random number generation

# sets the global variables
win_count = 0
loss_count = 0
tie_count = 0
game_count = 0


# This function includes a loop that iterates as long as the user continues to play.
# Calls get_choices function to get the player and computer choices.
# Calls play_game function with the choices to decide the winner/tie
# Calls display_summary_results function to display total games, wins, losses, and ties
# Important: do NOT change the 3 statements provided. You will need to add code to complete
#    this function, but you CANNOT change these statements.

def main():
    play_again = "yes"
    while play_again == "yes":
        computer_choice, player_choice = get_choices()
        play_again = play_game(computer_choice, player_choice)
        global game_count
        game_count = game_count + 1
    display_summary_results()


# This function uses the random.choice method to generate the computer's choice (rock, paper, or scissors).
# Prompts the player for their choice.
# If an invalid value is entered, continue to prompt until a valid value is provided.
# Important: Do NOT change the 2 statements provided. You will need to add code to complete the function.
def get_choices():
    invalid_choice = "yes"
    valid_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(valid_choices)
    while invalid_choice == "yes":
        player_choice = input('Enter choice (rock, paper, scissors):')
        if player_choice in valid_choices:
            invalid_choice = "no"
        else:
            invalid_choice = "yes"
            print("Try again. Enter rock, paper or scissors")
    return computer_choice, player_choice


# This function determines the winner/tie based on the computer and player's choices that are passed to this function.
# Prints the choices, and checks the possible combinations to determine the winner/tie.
# Prints the result, e.g., 'Computer wins!', 'You win!', or 'it's a tie!'
# Keeps track of the number of wins/losses/ties so far.
def play_game(computer, player):
    if computer == 'rock':
        if player == 'rock':
            print("Your choice: rock")
            print("Computer's choice: rock")
            print("it's a tie!")
            global tie_count
            tie_count = tie_count + 1
        elif player == 'scissors':
            print("Your choice: scissors")
            print("Computer's choice: rock")
            print("Computer wins!")
            global loss_count
            loss_count = loss_count + 1
        else:
            print("Your choice: paper")
            print("Computer's choice: rock")
            print("You win!")
            global win_count
            win_count = win_count + 1
    elif computer == 'scissors':
        if player == 'rock':
            print("Your choice: rock")
            print("Computer's choice: scissors")
            print("You win!")
            win_count = win_count + 1
        elif player == 'scissors':
            print("Your choice: scissors")
            print("Computer's choice: scissors")
            print("it's a tie")
            tie_count = tie_count + 1
        else:
            print("Your choice: paper")
            print("Computer's choice: scissors")
            print("Computer wins!")
            loss_count = loss_count + 1
    else:
        if player == 'rock':
            print("Your choice: rock")
            print("Computer's choice: paper")
            print("Computer wins!")
            loss_count = loss_count + 1
        elif player == 'scissors':
            print("Your choice: scissors")
            print("Computer's choice: paper")
            print("You win!")
            win_count = win_count + 1
        else:
            print("Your choice: paper")
            print("Computer's choice: paper")
            print("it's a tie")
            tie_count = tie_count + 1
    user_again = input('Play again? (yes/no)')
    return user_again


# Once the player has decided to stop playing, display total number of games, wins, losses, and ties
# Hint: you may use global variables to accumulate wins, losses, and ties
def display_summary_results():
    print("You played ", game_count, "games")
    print(win_count, "wins")
    print(loss_count, "losses")
    print(tie_count, "ties")


main()
