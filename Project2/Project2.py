#
#PROJECT 2: ROCK, PAPER, SCISSORS GAME
#

print(" WELCOME!!! ".center(50,"#"))
print("\n")
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

options = ["rock", "paper", "scissors"]

player1_input = input("Type Rock/Paper/Scissors: ").lower()

if player1_input not in options:
    print("Invalid option entered by player1")

player2_input = input("Type Rock/Paper/Scissors: ").lower()

if player2_input not in options:
    print("Invalid option entered by player2")

if player1_input == "rock" and player2_input == "scissors":
    print(f"{player1} won!")

elif player1_input == "paper" and player2_input == "rock":
    print(f"{player1} won!")

elif player1_input == "scissors" and player2_input == "paper":
    print(f"{player1} won!")

elif player1_input == player2_input:
    print("It is a draw")

else:
    print(f"{player2} won!")

print("Goodbye!")
