import random

ans = input("Wanna Play? ")

while ans.lower() == "yes":
    list = ["Rock","Paper","Scissors"]
    random.shuffle(list)
    computer = random.choice(list)
    player = input("Rock/Paper/Scissors? ")
    print("Player: "+player)
    print("Computer: "+computer)
    if computer == player:
        print("Tie!!")
    elif computer == "Rock":
        if player == "Scissors":
            print("Player Loose!!")
        elif player == "Paper":
            print("Player Wins!!!!!")
    elif computer == "Scissors":
        if player == "Paper":
            print("Player Loose!!")
        elif player == "Rock":
            print("Player Wins!!!!!")
    elif computer == "Paper":
        if player == "Rock":
            print("Player Loose!!")
        elif player == "Scissors":
            print("Player Wins!!!!!")
    ans = input("Wanna Play Again? ")

print("Comeback and play :(")

