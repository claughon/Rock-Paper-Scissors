import random

def RPC():
    player_win = 0
    comp_win = 0
    ties = 0
    while True:
        player_choice = input("Rock, Paper, Scissors? type 'Quit' to quit ")
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        if player_choice.title() == "Quit":
            print(f"The final score was {player_win} to {comp_win}")
            break
        elif player_choice.title() == comp_choice:
            ties += 1
            print(f"You both chose {player_choice}, it's a tie!")
        elif player_choice.title() == "Rock" and comp_choice == "Scissors":
            player_win +=1
            print(f"Your opponent chose Scissors, you chose Rock, you win!")
        elif player_choice.title() == "Rock" and comp_choice == "Paper":
            print(f"Your opponent chose Paper, you chose Rock, you lose!")
            comp_win +=1
        elif player_choice.title() == "Scissors" and comp_choice == "Rock":
            print(f"Your opponent chose Rock, you chose Scissors, you lose!")
            comp_win +=1
        elif player_choice.title() == "Scissors" and comp_choice == "Paper":
            print(f"Your opponent chose Paper, you chose Scissors, you win!")
            player_win +=1
        elif player_choice.title() == "Paper" and comp_choice == "Scissors":
            print(f"Your opponent chose Scissors, you chose Paper, you lose!")
            comp_win +=1
        elif player_choice.title() == "Paper" and comp_choice == "Rock":
            print(f"Your opponent chose Rock, you chose Paper, you win!")
            player_win +=1    
        else:
            print("Please input a valid option")
RPC()