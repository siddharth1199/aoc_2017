from itertools import combinations
from functools import reduce
from itertools import groupby
from math import ceil
import sys

PLAYER_HIT_POINTS = 100
NUM_RINGS = 2

WEAPONS = [
    ('Dagger', 8, 4),
    ('Shortsword', 10, 5),
    ('Warhammer', 25, 6),
    ('Longsword', 40, 7),
    ('Greataxe', 74, 8)
]

ARMOR = [
    ('', 0, 0),
    ('Leather', 13, 1),
    ('Chainmail', 31, 2),
    ('Splintmail', 53, 3),
    ('Bandedmail', 75, 4),
    ('Platemail', 102, 5)
]

DAMAGE_RINGS = [
    ('Damage +1', 25, 1),
    ('Damage +2', 50, 2),
    ('Damage +3', 100, 3)
]

DEFENSE_RINGS = [
    ('Defense +1', 20, 1),
    ('Defense +2', 40, 2),
    ('Defense +3', 80, 3)
]


def parse_input(filepath):
    stats = dict()

    with open(filepath, 'r') as f:
        for line in f:
            k, v = line.split(': ')
            stats[k] = int(v)

    return (stats['Hit Points'], stats['Damage'], stats['Armor'])


def equipment_sum(e1, e2):
    name1, cost1, value1 = e1
    name2, cost2, value2 = e2
    return (name1 + ' - ' + name2, cost1 + cost2, value1 + value2)


def att_def_equipment_sum(att_equipment, def_equipment):
    att_name, att_cost, att_value = att_equipment
    def_name, def_cost, def_value = def_equipment
    result = (
        def_name + ' - ' + att_name,
        att_cost + def_cost,
        att_value,
        def_value
    )
    return result


def get_ring_combinations(rings, num_rings):
    default_ring = ('', 0, 0)
    result = [
        reduce(equipment_sum, c, default_ring) for c in combinations(rings, num_rings)
    ]
    return result


def get_all_ring_combinations(rings, max_num_rings):
    ring_combinations = {
        i: get_ring_combinations(rings, i)
        for i in range(max_num_rings + 1)
    }
    return ring_combinations


def get_ring_equipment_combinations(rings, max_num_rings, equipment_list):
    rings_dict = get_all_ring_combinations(rings, max_num_rings)
    
    ring_equipment_combos = {
        i: [equipment_sum(a, r) for a in equipment_list for r in l]
        for i, l in rings_dict.items()
    }

    return ring_equipment_combos


def get_dmg_done(attack_dmg, defend_armor):
    return max(attack_dmg - defend_armor, 1)


def get_attacks_until_death(player_armor, player_hp, boss_dmg):
    dmg_per_attack = get_dmg_done(boss_dmg, player_armor)
    return ceil(player_hp/dmg_per_attack)


def get_lowest_winning_dmg(boss_hp, boss_armor, attacks_until_death):
    lowest_hp_lost_per_turn = ceil(boss_hp/attacks_until_death)
    if lowest_hp_lost_per_turn == 1:
        return 0
    else:
        return lowest_hp_lost_per_turn + boss_armor


def get_equipment_combinations(
    boss_stats, defense_ring_combos, attack_ring_combos):
    boss_hp, boss_dmg, boss_armor = boss_stats
    
    for num_defense_rings, def_equipment_list in defense_ring_combos.items():
        att_equipment_list = [
            e
            for i, l in attack_ring_combos.items()
            if i <= NUM_RINGS - num_defense_rings
            for e in l
        ]
        
        for def_name, def_cost, def_value in def_equipment_list:
            attacks_until_death = get_attacks_until_death(
                def_value, PLAYER_HIT_POINTS, boss_dmg
            )
            
            lowest_winning_dmg = get_lowest_winning_dmg(
                boss_hp, boss_armor, attacks_until_death
            )
            
            for att_name, att_cost, att_value in att_equipment_list:
                equip = (
                    def_name + ' - ' + att_name,
                    att_cost + def_cost,
                    att_value,
                    def_value
                )
                if att_value >= lowest_winning_dmg:
                    yield (*equip, True)
                else:
                    yield (*equip, False)


def get_extreme_equipment_combinations(boss_stats):
    defense_ring_combos = get_ring_equipment_combinations(
        DEFENSE_RINGS, NUM_RINGS, ARMOR
    )

    attack_ring_combos = get_ring_equipment_combinations(
        DAMAGE_RINGS, NUM_RINGS, WEAPONS
    )

    equipment_combinations = get_equipment_combinations(
        boss_stats, defense_ring_combos, attack_ring_combos
    )
    
    min_winning_cost = 1e9
    max_losing_cost = 0

    for equip_combo in equipment_combinations:
        _, cost, *_, winning = equip_combo
        if winning and (cost < min_winning_cost):
            min_winning_cost = cost
            min_winning_equip = equip_combo
        elif (not winning) and (cost > max_losing_cost):
            max_losing_cost = cost
            max_losing_equip = equip_combo

    return min_winning_equip, max_losing_equip


def print_equipment(equipment):
    equip_name, equip_cost, att_value, def_value, _ = equipment

    print("Equipment used: {}".format(equip_name))
    print("Cost: {}".format(equip_cost))
    print("Attack value: {}".format(att_value))
    print("Armor value: {}".format(def_value))


def main(filepath):
    boss_stats = parse_input(filepath)

    min_winning_equip, max_losing_equip = get_extreme_equipment_combinations(boss_stats) 
    
    print("\nCheapest winning equipment:\n")
    print_equipment(min_winning_equip)

    print("\nMost expensive losing equipment:\n")
    print_equipment(max_losing_equip)


if __name__=='__main__': 
    if len(sys.argv) > 1: 
        filepath = sys.argv[1] 
    else: 
        filepath = "input.txt" 
    main(filepath) 
