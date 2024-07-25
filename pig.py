import random

class Player:
    def __init__(self, score):
        self.score = score

def pig(score):
    roll = 0
    while roll != 1:
        roll = random.randint(1, 6)
        print(f"You rolled {roll}.")
        if roll != 1:
            score += roll
            print(f"Your score is now {score}.")
            cont = input("Would you like to continue (y/n)? ")
            if cont == "n":
                break
        else:
            score = 0
            print("Your score is now 0.")
    return score

print("Player 1's Turn")
p1 = Player(0)
print("Player 2's Turn")
p2 = Player(0)

p1.score = pig(p1.score)
p2.score = pig(p2.score)

print(f"Player 1's final score: {p1.score}")
print(f"Player 2's final score: {p2.score}")

if p1.score > p2.score:
    print("Player 1 wins!")
elif p1.score < p2.score:
    print("Player 2 wins!")
else:
    print("It's a tie!")