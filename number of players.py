import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll


while True:
    players = int(input('enter the number of players (1=2-4): '))
    if 2 <= players <= 4:
        break
    else:
     print("players must be between 2 - 4")
else:
   print("invalid, try again")
    
print("You've entered a valid number of players:", players)

