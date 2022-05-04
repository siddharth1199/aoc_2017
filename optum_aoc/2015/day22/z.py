'''
Day 22 Advent of Code, RPG
At first I tried to make my decision function rules based, to find the best solution in 1 go
that didnt work, so now I am introducing randomness to see if I try many differnet things will I get lucky
and find the right solution.

i also included in this code a way to give the character a list of instructions to carry out, this is the
cheat code method. I added this for debugging to make sure that my battle simulator matches the advent of
code example (which it does, except a print statement for armour but the actual mechanic works).

But I still have not found the right answer :(

'''

import sys
import time
from random import randint

PLAYER_START_HP = 50
PLAYER_START_MANA = 500

SPELLS_COST = {
    'missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}

SPELLS_DURATION = {
    'missile': 0,
    'drain': 0,
    'shield': 6,
    'poison': 6,
    'recharge': 5
}

SPELLS_POWER = {
    'missile': 4,
    'drain': 2,
    'shield': 7,
    'poison': 3,
    'recharge': 101
}


def parser(file_loc):
    ''' Reads input and returns boss stats as list [hit points, damage] '''
    boss_stats = []
    with open(file_loc, "r") as myfile:
        for line in myfile:
            boss_stats.append(int(line.split()[-1]))
    return boss_stats


def apply_status(player_info, boss_info, effects_info):
    """ This is a subroutine, it acts directly on dictionaries in the main body """
    if effects_info['shield'] > 0:
        player_info['armour'] = SPELLS_POWER['shield']
        effects_info['shield'] -= 1
    else:
        player_info['armour'] = 0

    if effects_info['poison'] > 0:
        boss_info['hp'] -= SPELLS_POWER['poison']
        effects_info['poison'] -= 1

    if effects_info['recharge'] > 0:
        player_info['mana'] += SPELLS_POWER['recharge']
        effects_info['recharge'] -= 1

    return None


def decision_making(player_info, boss_info, effects_info):
    """ decides what spell to cast

    this applies some logic at first to pick the best spell if there is obviously a best choice
    otherwise it picks a spell at random

    """
    # if we can kill boss now lets do it
    if effects_info['poison'] > 0:
        if boss_info['hp'] < SPELLS_POWER['missile'] + SPELLS_POWER['poison']:
            return 'missile'
    else:
        if boss_info['hp'] < SPELLS_POWER['missile']:
            return 'missile'

    # if we are about to run out of magic, lets recharge
    if effects_info['recharge'] == 0:
        if player_info['mana'] <= SPELLS_COST['recharge'] + SPELLS_COST['poison']:  # enough for recharge and other most expensive spell
            return 'recharge'

    # if we are on 1 health lets heal
    if player_info['hp'] == 1:  # this logic could be improved
        return 'drain'

    # what to do in standard situation
    random_list = ['missile', 'drain', 'shield', 'poison', 'recharge']

    # remove spells that cannot be used due to effect already being active
    if effects_info['shield'] > 0:
        random_list.remove('shield')
    if effects_info['poison'] > 0:
        random_list.remove('poison')
    if effects_info['recharge'] > 0:
        random_list.remove('recharge')

    # pick random spell from random_list
    num_spells_available = len(random_list)
    return random_list[randint(0, num_spells_available-1)]


def cheat_codes(correct_moves):
    """ this is a generator
    tell player what move to do, useful for debugging if you give list of spells to use"""
    for move in correct_moves:
        yield move


def player_turn(player_info, boss_info, effects_info, total_mana_spend, correct_move_generator=None, verbose=False):
    """ conducts calculations for a players turn,
    this is a subroutine it acts directly on the dictionariers in the main body """
    boss_dead = False
    player_dead = False

    if verbose:
        print(f'at start of player turn, {player_info}, {boss_info}, {effects_info}')

    # apply status
    apply_status(player_info, boss_info, effects_info)
    if boss_info['hp'] <= 0:
        boss_dead = True
        return boss_dead, total_mana_spend, 'nothing_boss_already_dead', player_dead

    # decide what spell to cast
    if correct_move_generator:
        spell_choice = next(correct_move_generator)
    else:
        spell_choice = decision_making(player_info, boss_info, effects_info)
    if verbose:
        print(f'spell choice is {spell_choice}')

    # pay spells mana cost and add to total mana spend
    if player_info['mana'] < SPELLS_COST[spell_choice]:
        player_dead = True
        return boss_dead, total_mana_spend, 'ran out of mana casting {}'.format(spell_choice), player_dead

    player_info['mana'] -= SPELLS_COST[spell_choice]
    total_mana_spend += SPELLS_COST[spell_choice]

    # do spell
    if spell_choice == 'missile':
        boss_info['hp'] -= SPELLS_POWER['missile']
    elif spell_choice == 'drain':
        boss_info['hp'] -= SPELLS_POWER['drain']
        player_info['hp'] += SPELLS_POWER['drain']
    elif spell_choice == 'shield':
        effects_info['shield'] = SPELLS_DURATION['shield']
    elif spell_choice == 'poison':
        effects_info['poison'] = SPELLS_DURATION['poison']
    elif spell_choice == 'recharge':
        effects_info['recharge'] = SPELLS_DURATION['recharge']
    else:
        print('invalid spell choice')

    if boss_info['hp'] <= 0:
        boss_dead = True

    if verbose:
        print(f'at end of player turn, {player_info}, {boss_info}, {effects_info}')

    return boss_dead, total_mana_spend, spell_choice, player_dead


def boss_turn(player_info, boss_info, effects_info, verbose=False):
    """ conducts calculations for a boss turn,
    this is a subroutine it acts directly on the dictionariers in the main body """
    player_dead = False
    boss_dead = False

    if verbose:
        print(f'at start of boss turn, {player_info}, {boss_info}, {effects_info}')

    # apply status
    apply_status(player_info, boss_info, effects_info)

    # Check if boss died
    if boss_info['hp'] <= 0:
        boss_dead = True
        return player_dead, boss_dead


    # do attack
    theory_damage = boss_info['damage'] - player_info['armour']
    actual_damage = max(1, theory_damage)
    player_info['hp'] -= actual_damage

    if player_info['hp'] <= 0:
        player_dead = True

    if verbose:
        print(f'at end of boss turn, {player_info}, {boss_info}, {effects_info}')

    return player_dead, boss_dead


def battle(player_info, boss_info, effects_info, correct_moves=None, verbose=False):
    """ simulates battle """
    # initilise battle
    total_mana_spend = 0
    player_dead = False
    boss_dead = False
    player_choice_list = []

    if correct_moves:
        correct_move_generator = cheat_codes(correct_moves)
    else:
        correct_move_generator = None

    while boss_dead == player_dead == False:
        # player turn
        boss_dead, total_mana_spend, spell_choice, player_dead = player_turn(player_info, boss_info, effects_info,
                                                                             total_mana_spend, correct_move_generator, verbose)
        player_choice_list.append(spell_choice)
        # boss turn
        player_dead, boss_dead = boss_turn(player_info, boss_info, effects_info, verbose)

    if boss_dead:
        victory = True
    else:
        victory = False

    return total_mana_spend, victory, player_choice_list


def many_battles(n, file_loc, verbose=False):
    """ this does many random battles """
    i = 0
    lowest_mana_spend = 100000000
    best_battle_strategy = []
    win = False

    while i < n:
        # need to re initilise player, boss and effect stats every time as sub routine
        enemy_details = parser(file_loc)
        boss_stats = {
            'hp': enemy_details[0],
            'damage': enemy_details[1]
        }

        player_stats = {
            'hp': PLAYER_START_HP,
            'armour': 0,
            'mana': PLAYER_START_MANA
        }

        current_timer = {
            'shield': 0,
            'poison': 0,
            'recharge': 0
        }

        total_mana_spend, victory, player_choice_list = battle(player_stats, boss_stats, current_timer, verbose=verbose)
        if victory:
            win = True
            if total_mana_spend < lowest_mana_spend:
                lowest_mana_spend = total_mana_spend
                best_battle_strategy = player_choice_list

        i += 1
        if i % 100 == 0:
            print('simulating battle number {}'.format(i))
            print('so far best battle cost {}, the spell choices were {}, and we won {}'.format(lowest_mana_spend,
                                                                                                best_battle_strategy,
                                                                                                win))
    return lowest_mana_spend, best_battle_strategy, win

if __name__ == '__main__':
    start_time = time.time()
    input_file = 'Day22_input.txt'

    if len(sys.argv) >= 2:
        input_file = sys.argv[1]


    # random battle
    n_battles = 1000
    full_mana_cost, spells_chosen, winner = many_battles(n_battles, input_file, verbose=False)
    if winner:
        print(f'we won the fight {winner}, the total mana cost of the fight was {full_mana_cost} and the spell choice was {spells_chosen}')

    """
    # Use cheat codes
    good_moves = ['recharge', 'shield', 'drain', 'poison', 'missile']

    # initilise single battle for cheat codes
    enemy_details = parser(input_file)
    boss_stats = {
        'hp': enemy_details[0],
        'damage': enemy_details[1]
    }

    player_stats = {
        'hp': PLAYER_START_HP,
        'armour': 0,
        'mana': PLAYER_START_MANA
    }

    current_timer = {
        'shield': 0,
        'poison': 0,
        'recharge': 0
    }
    full_mana_cost, winner, spells_chosen = battle(player_stats, boss_stats, current_timer, correct_moves=good_moves, verbose=True)
    """

    end_time = time.time()
    duration = end_time - start_time
    print('The code took {:.2f} seconds to execute'.format(duration))
