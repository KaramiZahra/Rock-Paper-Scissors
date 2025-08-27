import random

options = ["Rock", "Paper", "Scissors"]
options_map = {"1": "Rock", "2": "Paper", "3": "Scissors"}

rounds = int(input("How many rounds do you want to play? "))
player_score = 0
computer_score = 0

while rounds > 0:
    print("\n1)Rock  2)Paper  3)Scissors")
    player_choose_move = input("Choose your move: ")

    if player_choose_move not in options_map:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    player_move = options_map[player_choose_move]
    computer_move = random.choice(options)
    print(f"You chose {player_move}, Computer chose {computer_move}")

    # winner logic
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == "Rock" and computer_move == "Scissors") or (player_move == "Paper" and computer_move == "Rock") or (player_move == "Scissors" and computer_move == "Paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    rounds -= 1

# final result
print("\n=== Game Over ===")
if player_score > computer_score:
    print("🎉 You won the game!")
elif computer_score > player_score:
    print("💻 Computer won the game!")
else:
    print("🤝 It's a tie overall!")
