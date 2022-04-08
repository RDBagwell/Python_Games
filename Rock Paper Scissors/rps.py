import imp

import random

def play():
    usser = input("'R' for Rock, 'P' for paper, 'S' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if(usser == computer):
        return 'tie'

    if is_win(usser, computer):
        return "Player Wins"

    return "Computer Wins"


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())
