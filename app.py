import random


options = ["Rock", "Paper", "Scissors"]
options_map = {"1": "Rock", "2": "Paper", "3": "Scissors"}


class Player:
    def __init__(self, name, is_computer=False, score=0):
        self.name = name
        self.is_computer = is_computer
        self.score = score

    def choose_move(self):
        if self.is_computer:
            return random.choice(options)
        else:
            while True:
                print("\n1)Rock  2)Paper  3)Scissors")
                player_choice = input("Choose your move: ")

                if player_choice in options_map:
                    return options_map[player_choice]
                print("Invalid choice!")


class Game:
    def __init__(self, rounds, player1, player2):
        self.rounds = rounds
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        player1_move = self.player1.choose_move()
        player2_move = self.player2.choose_move()
        print(
            f"{self.player1.name} chose {player1_move}, {self.player2.name} chose {player2_move}")

        self.decide_winner(player1_move, player2_move)

    def decide_winner(self, player1_move, player2_move):
        if player1_move == player2_move:
            print("It's a tie!")
        elif (player1_move == "Rock" and player2_move == "Scissors") or (player1_move == "Paper" and player2_move == "Rock") or (player1_move == "Scissors" and player2_move == "Paper"):
            print(f"{self.player1.name} wins this round!")
            self.player1.score += 1
        else:
            print(f"{self.player2.name} wins this round!")
            self.player2.score += 1

    def play(self):
        while self.rounds > 0:
            self.play_round()
            self.rounds -= 1

        # final results
        print("\n=== Game Over ===")
        if self.player1.score > self.player2.score:
            print(f"🎉 {self.player1.name} won the game!")
        elif self.player2.score > self.player1.score:
            print(f"💻 {self.player2.name} won the game!")
        else:
            print("🤝 It's a tie overall!")


rounds = int(input("How many rounds do you want to play? "))
player1 = Player("Alice")
player2 = Player("Computer", True)
game = Game(rounds, player1, player2)
game.play()
