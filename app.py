import random

options = ["Rock", "Paper", "Scissors"]
options_map = {"1": "Rock", "2": "Paper", "3": "Scissors"}


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def choose_move(self):
        if self.name == "Computer":
            return random.choice(options)
        else:
            while True:
                print("\n1)Rock  2)Paper  3)Scissors")
                player_choice = input("Choose your move: ")

                if player_choice in options_map:
                    return options_map[player_choice]
                print("Invalid choice! Please enter 1, 2, or 3.")


class Game:
    def __init__(self, rounds, player, computer):
        self.rounds = rounds
        self.player = player
        self.computer = computer

    def play_round(self):
        player_move = self.player.choose_move()
        computer_move = self.computer.choose_move()
        print(f"You chose {player_move}, Computer chose {computer_move}")

        self.decide_winner(player_move, computer_move)

    def decide_winner(self, player_move, computer_move):
        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "Rock" and computer_move == "Scissors") or (player_move == "Paper" and computer_move == "Rock") or (player_move == "Scissors" and computer_move == "Paper"):
            print("You win this round!")
            self.player.score += 1
        else:
            print("Computer wins this round!")
            self.computer.score += 1

    def play(self):
        while self.rounds > 0:
            self.play_round()
            self.rounds -= 1

        # final results
        print("\n=== Game Over ===")
        if self.player.score > self.computer.score:
            print("🎉 You won the game!")
        elif self.computer.score > self.player.score:
            print("💻 Computer won the game!")
        else:
            print("🤝 It's a tie overall!")


rounds = int(input("How many rounds do you want to play? "))
player = Player("You")
computer = Player("Computer")
game = Game(rounds, player, computer)
game.play()
