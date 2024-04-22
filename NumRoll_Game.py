import random

def singleplayer():
    info = {'Computer':0}
    n = input('Enter your name : ')
    info[n] = 0
    h = int(input('Set the score limit : '))
    round = 1
    while(max(info.values()) < h):
        choices = ['x', 'y', 'z']
        x,y,z = random.randint(0,9) , random.randint(0,9) , random.randint(0,9)
        print(f'Round {round} : ')
        player_choice = input(f"{n}'s choice (x/y/z) : ")
        if player_choice=='x':
            info[n] += x
        elif player_choice=='y':
             info[n] += y
        elif player_choice=='z':
             info[n] += z
        else:
             print('Invalid choice !!')
        computer_choice = random.choice(choices)
        print(f"Computer's choice : {computer_choice}")
        if computer_choice == 'x':
            info['Computer'] += x
        elif computer_choice == 'y':
            info['Computer'] += y
        elif computer_choice == 'z':
            info['Computer'] += z
        else:
            print('Invalid choice !!')
        print(f'Round {round} Tokens: x={x} , y={y} , z={z}')
        print(f'Current Results: {info}')
        round += 1
    for player, score in info.items():print(f'{player} : {score}')
    max_score = max(info.values())
    winners = [player for player, score in info.items() if score == max_score]
    if len(winners) == 1:
        print(f"The winner is {winners[0]} !")
    else:
        print("The winners are:", ", ".join(winners))
    print('Game over !')

def multiplayer():
    info = {}
    players= input('Enter names of all players (Ex: a,b,c) : ')
    players_list = players.split(',')
    for p in players_list:
        info[p.strip()] = 0
    h = int(input('Set the score limit : '))
    round = 1
    while(max(info.values()) < h):
        x,y,z = random.randint(0,9) , random.randint(0,9) , random.randint(0,9)
        print(f'Round {round} : ')
        for i in info.keys():
            c = input(f"{i}'s choice (x/y/z) : ")
            if c=='x':
                info[i] += x
            elif c=='y':
                info[i] += y
            elif c=='z':
                info[i] += z
            else:
                print('Invalid choice !!')
        print(f'Round {round} Tokens: x={x} , y={y} , z={z}')
        print(f'Current Results: {info}')
        round += 1
    for player, score in info.items():print(f'{player} : {score}')
    max_score = max(info.values())
    winners = [player for player, score in info.items() if score == max_score]
    if len(winners) == 1:
        print(f"The winner is {winners[0]} !")
    else:
        print("The winners are:", ", ".join(winners))
    print('Game over !')

print('Welcome to NumRoll !')
print("""HOW TO PLAY : 
    After starting a new game, select a mode, either single-player or multiplayer.
    One of the player has to set a maximum score limit before continuing the game. 
    Each player will be given a choice of 3 tokens x, y and z.
    Each token will contain a random number number between 0 and 9.
    For every round each player must enter their token choices. 
    The choices must be either x or y or z.
    For every choice in each round the token number will be added to the players' score.
    The first player to reach the maximum score wins the game.
    Remember this game is completely based on luck.
    BEST OF LUCK !!""")
command = input('New Game (n) / Exit (e) : ')
while command != 'e':
    if command == 'n':
        mode = input('Play with computer (c) / Multiplayer (m): ')
        if mode == 'c':
            singleplayer()
        elif mode == 'm':
            multiplayer()
        else:
            print('Invalid mode selected !!')
    command = input('New Game (n) / Exit (e): ')
print('Goodbye !!')