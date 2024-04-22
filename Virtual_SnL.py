import random

def singleplayer():
    position = {'Computer': 0}
    n = input('Enter your name : ')
    position[n] = 0
    while max(position.values()) != 100:
        for i in position.keys():
            print(f"{i}'s roll : ")
            if i == n:
                r = input("Press r to roll the die : ")
                die_number = random.randint(1,6)
                print(f"You rolled {die_number}!")
            else:
                input("Computer's turn - Press Enter to continue.")
                die_number = random.randint(1,6)
                print(f"Computer rolled {die_number}!")
            cur_position = position[i] + die_number
            if position[i] == 0:
                if die_number == 1:
                    position[i] = 1
                else:
                    position[i] = 0
            elif cur_position > 100:
                position[i] = cur_position - die_number
            else:
                if cur_position == 4:
                    print('Yayy, you got a ladder !!')
                    position[i] = 25
                elif cur_position == 21:
                    print('Yayy, you got a ladder !!')
                    position[i] = 39
                elif cur_position == 29:
                    print('Yayy, you got a ladder !!')
                    position[i] = 74
                elif cur_position == 30:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 7
                elif cur_position == 43:
                    print('Yayy, you got a ladder !!')
                    position[i] = 76
                elif cur_position == 47:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 15
                elif cur_position == 56:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 19
                elif cur_position == 63:
                    print('Yayy, you got a ladder !!')
                    position[i] = 80
                elif cur_position == 71:
                    print('Yayy, you got a ladder !!')
                    position[i] = 89
                elif cur_position == 73:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 51
                elif cur_position == 82:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 42
                elif cur_position == 92:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 75
                elif cur_position == 98:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 55
                else:
                    position[i] = cur_position
        print(f"Current positions : {position}")
    max_score = max(position.values())
    winners = [player for player, score in position.items() if score == max_score]
    final_positions = position.copy()
    print("Game Over!")
    for player, score in final_positions.items():
        print(f"{player} : {score}")
    if len(winners) == 1:
        print(f"The winner is {winners[0]}!")
    else:
        print("The winners are:", ", ".join(winners))

def multiplayer():
    position = {}
    players = input('Enter names of all players (Ex: a,b,c) : ')
    players_list = players.split(',')
    for p in players_list:
        position[p.strip()] = 0
    if(len(players_list) < 2 or len(players_list) > 4):
        print('Maximum 4/minimum 2 players can play.')
    while(max(position.values())!=100):
        for i in position.keys():
            print(f"{i}'s roll : ")
            r = input('Press r to roll the die : ')
            die_number = random.randint(1,6)
            print(f"You rolled {die_number} !") if(r=='r') else print('Invalid command !!')
            cur_position = position[i]+die_number
            if position[i] == 0:
                if die_number == 1:
                    position[i] = 1
                else:
                    position[i] = 0
            elif cur_position > 100:
                position[i] = cur_position - die_number
            else:
                if cur_position == 4:
                    print('Yayy, you got a ladder !!')
                    position[i] = 25
                elif cur_position == 21:
                    print('Yayy, you got a ladder !!')
                    position[i] = 39
                elif cur_position == 29:
                    print('Yayy, you got a ladder !!')
                    position[i] = 74
                elif cur_position == 30:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 7
                elif cur_position == 43:
                    print('Yayy, you got a ladder !!')
                    position[i] = 76
                elif cur_position == 47:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 15
                elif cur_position == 56:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 19
                elif cur_position == 63:
                    print('Yayy, you got a ladder !!')
                    position[i] = 80
                elif cur_position == 71:
                    print('Yayy, you got a ladder !!')
                    position[i] = 89
                elif cur_position == 73:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 51
                elif cur_position == 82:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 42
                elif cur_position == 92:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 75
                elif cur_position == 98:
                    print('Damn, you got bit by a snake !!')
                    position[i] = 55
                else:
                    position[i] = cur_position
        print(f"Current positions : {position}")
    max_score = max(position.values())
    winners = [player for player, score in position.items() if score == max_score]
    final_positions = position.copy()
    print("Game Over!")
    for player, score in final_positions.items():
        print(f"{player} : {score}")
    if len(winners) == 1:
        print(f"The winner is {winners[0]}!")
    else:
        print("The winners are:", ", ".join(winners))

print("""Welcome to Virtual Snakes and Ladders !
This is a virtual version of the famous board game Snakes and Ladders.
ENJOY !!""")
print("""HOW TO PLAY : 
    After starting new game, select to play with computer or a multiplayer game.
    Each player has to roll die for their turn by clicking r key in keyboard.
    The first player to reach the 100th position wins the Snakes AND Ladders.
    Remember, this game is based on luck , so watch out for the snakes and BEST OF LUCK!!""")
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