actions = ['attack', 'go', 'check']
directions = ['next room', 'previous room']
enemies = ['spider', 'bug', 'snake', 'wolf']
filler = ['from', 'with', 'to']
weapons = ['wood_sword', 'iron_sword', 'steel_mace', 'steel_sword', 'steel_dagger', 'iron_dagger']
lexicon = {
            "actions": actions,
            "filler": filler,
            "enemies": enemies,
            "weapons": weapons
           }

def attack(target, weapon):
    print(f'attack {target} with {weapon}')


def parse_input(player_input, target):
    action = str
    words = player_input.split()
    # print(words)

    if words[0] in actions:
        if words[1] in enemies:
            if words[1].capitalize() == target.name:
                if words[3] in weapons:
                    return words[3]
            else:
                print("Wrong enemy.")
                return 0
        else:
            print("\nThis enemy does not exists.\n")
            return 0
        #action = words[0]
    else:
        print(words[0], 'is not a recognized action.')
        return 0


#parse_input(input())
