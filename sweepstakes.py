import random

player_count = int(input("How many people are playing?: "))

if player_count % 4 != 0:
    raise ValueError("Number of players must be a factor of 32")
elif player_count > 32:
    raise ValueError("Number of players can't exceed 32")
elif player_count < 2:
    raise ValueError("Number of players must be at least 2")
else:
    pass

team_chunks = int(32/player_count)

teams_list = ["Brazil","Germany","Argentina","Australia","Belgium","Colombia","Costa Rica","Croatia","Denmark","Egypt","England","France","Iceland","Iran","Japan","Mexico","Morocco","Nigeria","Panama","Peru","Poland","Portugal","Russia","Saudi Arabia","Senegal","Serbia","South Korea","Spain","Sweden","Switzerland","Tunisia","Uruguay"]

random.shuffle(teams_list)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

counter = 0

for group in chunker(teams_list, team_chunks):
    counter = counter + 1
    print(f"Player {counter}, your teams are: ",group)
