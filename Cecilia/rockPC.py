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
            print("\U0001F9E8")	
            break
        elif player_choice.title() == comp_choice:
            ties += 1
            print(f"You both chose {player_choice}, it's a tie!")
        elif player_choice.title() == "Rock" and comp_choice == "Scissors":
            player_win +=1
            print(f"Your opponent chose Scissors, you chose Rock!")
            print(f"Rock CRUSHES Scissors, YOU WIN!!")
            print("\U0001FAA8")
        elif player_choice.title() == "Rock" and comp_choice == "Paper":
            print(f"Your opponent chose Paper, you chose Rock!")
            print(f"Paper SMOTHERS Rock, you LOSE!")
            print("\U0001F4DC")
            comp_win +=1
        elif player_choice.title() == "Scissors" and comp_choice == "Rock":
            print(f"Your opponent chose Rock, you chose Scissors!")
            print(f"Rock CRUSHES Scissors, you LOSE!")
            print("\U0001FAA8")
            comp_win +=1
        elif player_choice.title() == "Scissors" and comp_choice == "Paper":
            print(f"Your opponent chose Paper, you chose Scissors!")
            print(f"Scissors SLICE Paper, you WIN!")
            print("\U0001F5E1")
            player_win +=1
        elif player_choice.title() == "Paper" and comp_choice == "Scissors":
            print(f"Your opponent chose Scissors, you chose Paper!")
            print(f"Scissors SLICE Paper, you LOSE!")
            print("\U0001F5E1")
            comp_win +=1
        elif player_choice.title() == "Paper" and comp_choice == "Rock":
            print(f"Your opponent chose Rock, you chose Paper, you win!")
            print(f"Paper SMOTHERS Rock, you WIN!")
            print("\U0001F4DC")
            player_win +=1    
        else:
            print("Please input a valid option")
            print("\U0001F504")
RPC()