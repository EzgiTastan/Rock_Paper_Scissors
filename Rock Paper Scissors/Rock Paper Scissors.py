import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissor. What is your choice? \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie."

    if is_win(user, computer):
        return "You've won."
    return 'You lost!'

    #by the way, r > s, s > p, and p > r.
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())