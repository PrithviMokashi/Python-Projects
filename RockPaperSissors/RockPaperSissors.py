import random

def play():
    x = input("What your Choice? 'R' for Rock, 'P' for Paper, 'S' for Sissors : ").lower()
    play = random.choice(['r', 'p', 's'])
    if x == play:
        print("It's a Tie")
    if checkWin(x, play):
        print(f"Computer played {play}\nUser played {x}")
        print("User Wins!")
    else:
        print(f"Computer played {play}\nUser played {x}")
        print("Computer Wins!")


def checkWin(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    else:
        return False

play()