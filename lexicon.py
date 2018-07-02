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

weapon = None
action = None
enemy = None

def attack(target, weapon):
    print(f'attack {target} with {weapon}')


def parse_input(player_input, target):
    action = str
    words = player_input.split()
    # print(words)

    try:
        for word in words:
            if word in actions:
                action = word
                print(action)
            elif word in enemies:
                if word.capitalize() == target.name:
                    enemy = word
                else:
                    enemy = None
            elif word in weapons:
                weapon = word
            elif word in filler:
                pass
            else:
                action = None
                weapon = None

        if weapon and action and enemy:
            print(weapon)
            return weapon
        else:
            print("You gave a wrong input. Type with accuracy, will you?")
            return None

    except UnboundLocalError:
            print("\nSomething's missing in your input.\nTurn missed.")
            return None
#parse_input(input())
