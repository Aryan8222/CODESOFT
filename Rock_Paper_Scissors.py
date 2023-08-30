import tkinter as tk
import random

# Function to determine the winner of a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the game result
def update_result(result):
    result_label.config(text=result)

# Function to update the user and computer choices
def update_choices(user_choice, computer_choice):
    user_choice_label.config(text=f'Your Choice: {user_choice}')
    computer_choice_label.config(text=f'Computer Choice: {computer_choice}')

# Function to play a round of the game
def play_round(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    update_choices(user_choice, computer_choice)
    result = determine_winner(user_choice, computer_choice)
    update_result(result)
    update_scores(result)

# Function to reset the scores
def reset_scores():
    user_score.set(0)
    computer_score.set(0)
    ties.set(0)

# Function to update the scores
def update_scores(result):
    if result == "You win!":
        user_score.set(user_score.get() + 1)
    elif result == "Computer wins!":
        computer_score.set(computer_score.get() + 1)
    else:
        ties.set(ties.get() + 1)

# Function to start a new game
def new_game():
    update_result("")
    update_choices("", "")
    user_choice.set("")
    reset_scores()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create left frame for player's interface
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20)

# Create right frame for computer's interface
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=20)

# Boxes to display choices (Player's interface)
user_choice = tk.StringVar()
user_choice_label = tk.Label(left_frame, textvariable=user_choice, font=("Helvetica", 12))
user_choice_label.pack(pady=10)

# Boxes to display choices (Computer's interface)
computer_choice_label = tk.Label(right_frame, text="", font=("Helvetica", 12))
computer_choice_label.pack(pady=10)

# Buttons for rock, paper, and scissors (Player's interface)
rock_button = tk.Button(left_frame, text="Rock", width=10, height=2, bg="gray", fg="white", command=lambda: play_round('rock'))
paper_button = tk.Button(left_frame, text="Paper", width=10, height=2, bg="blue", fg="white", command=lambda: play_round('paper'))
scissors_button = tk.Button(left_frame, text="Scissors", width=10, height=2, bg="red", fg="white", command=lambda: play_round('scissors'))

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Labels to display result and scores
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

user_score = tk.IntVar()
computer_score = tk.IntVar()
ties = tk.IntVar()

user_score_label = tk.Label(left_frame, text="Your Score:", font=("Helvetica", 12))
user_score_value = tk.Label(left_frame, textvariable=user_score, font=("Helvetica", 12))
computer_score_label = tk.Label(right_frame, text="Computer Score:", font=("Helvetica", 12))
computer_score_value = tk.Label(right_frame, textvariable=computer_score, font=("Helvetica", 12))
ties_label = tk.Label(root, text="Ties:", font=("Helvetica", 12))
ties_value = tk.Label(root, textvariable=ties, font=("Helvetica", 12))

user_score_label.pack()
user_score_value.pack()
computer_score_label.pack()
computer_score_value.pack()
ties_label.pack()
ties_value.pack()

# Buttons for New Game and End Game
new_game_button = tk.Button(root, text="New Game", command=new_game)
end_game_button = tk.Button(root, text="End Game", command=root.quit)

new_game_button.pack(pady=10)
end_game_button.pack()

# Start a new game
new_game()

# Run the application
root.mainloop()
