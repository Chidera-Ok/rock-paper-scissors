import random

options = ["R", "P", "S"]
option_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
condition = True

while condition==True:
    player = input("Time to play Rock-Paper-Scissors!!! Dive right in. Choose R for Rock, P for Paper, S for Scissors: ")
    if player not in options:
        print('Choice of option invalid')
        continue
    else:
        cpu = random.choice(options)
        print(f'Player {option_dict[player]} : CPU {option_dict[cpu]}')
        if player == cpu:
            continue
        elif (player == 'R') & (cpu == 'S'):
            print('The Player won')
            break
        elif (player == 'P') & (cpu == 'R'):
            print('The Player won')
            break
        elif (player == 'S') & (cpu == 'P'):
            print('The Player won')
            break
        else:
            print('The CPU won')
            break

    
    


# Determine CPU_choice
CPU = random.choice("options")

# while true:
#     if player__choice == CPU_choice:
#         continue
#     elif player__choice