import random
choice = ["rock","paper","scissors"]
player_win_counter = 0
ai_win_counter = 0

def playerWin():
    print("You won!")
    global player_win_counter 
    player_win_counter += 1
    print(f"The new total score is \nYou: {player_win_counter} \nBot: {ai_win_counter}")
def playerLose():
    print("You lose!")
    global ai_win_counter
    ai_win_counter += 1
    print(f"The new total score is \nYou: {player_win_counter} \nBot: {ai_win_counter}")
def playerTie():
    print("It's a tie")
    print(f"The new total score is \nYou: {player_win_counter} \nBot: {ai_win_counter}")

def rockPaperScissors():
    user_input = ""
    while user_input != "quit":
        user_input = input("rock, paper or scissors?: ").lower()
        ai_choice = choice[random.randrange(0,3)]
        if user_input == "rock":
            if ai_choice == "rock":
                playerTie()
            elif ai_choice == "scissors":
                playerWin()
            elif ai_choice == "paper":
                playerLose()
        elif user_input == "paper":
            if ai_choice == "rock":
                playerWin()
            elif ai_choice == "scissors":
                playerLose()
            elif ai_choice == "paper":
                playerTie()
        elif user_input == "scissors":
            if ai_choice == "rock":
                playerLose()
            elif ai_choice == "scissors":
                playerTie()
            elif ai_choice == "paper":
                playerWin()
        else:
            print("Input rock, paper or scissors please.")

rockPaperScissors()