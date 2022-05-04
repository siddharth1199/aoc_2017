import collections
import itertools
import sys


Toon = collections.namedtuple('Toon', 'hp damage armor')
Gear = collections.namedtuple('Gear', 'cost damage armor name')

WEAPONS = [Gear(cost=8 , damage=4 , armor=0, name='Dagger'),
           Gear(cost=10 , damage=5 , armor=0, name='Shortsword'),
           Gear(cost=25 , damage=6 , armor=0, name='Warhammer'),
           Gear(cost=40 , damage=7 , armor=0, name='Longsword'),
           Gear(cost=74 , damage=8 , armor=0, name='Greataxe')]

ARMORS = [Gear(cost=0 , damage=0 , armor=0, name='no armor'),
          Gear(cost=13 , damage=0 , armor=1, name='Leather'),
          Gear(cost=31 , damage=0 , armor=2, name='Chainmail'),
          Gear(cost=53 , damage=0 , armor=3, name='Splintmail'),
          Gear(cost=75 , damage=0 , armor=4, name='Bandedmail'),
          Gear(cost=102 , damage=0 , armor=5, name='Platemail')]

RINGS = [Gear(cost=0 , damage=0 , armor=0, name='no ring'),
         Gear(cost=0 , damage=0 , armor=0, name='no ring'),
         Gear(cost=25 , damage=1 , armor=0, name='Damage +1'),
         Gear(cost=50 , damage=2 , armor=0, name='Damage +2'),
         Gear(cost=100 , damage=3 , armor=0, name='Damage +3'),
         Gear(cost=20 , damage=0 , armor=1, name='Defense +1'),
         Gear(cost=40 , damage=0 , armor=2, name='Defense +2'),
         Gear(cost=80 , damage=0 , armor=3, name='Defense +3')]


def read_boss(fname):
    with open(fname,'r') as f:
        return Toon(hp=int(f.readline().split(': ')[1]),
                    damage=int(f.readline().split(': ')[1]),
                    armor=int(f.readline().split(': ')[1]))
    
    
def player_wins(player, boss):
    boss_turns, boss_remainder = divmod(player.hp, max(boss.damage - player.armor, 1))
    if boss_remainder > 0: boss_turns += 1

    player_turns, player_remainder = divmod(boss.hp, max(player.damage - boss.armor, 1))
    if player_remainder > 0: player_turns += 1
    
    return player_turns <= boss_turns


def solve_brute_force(boss, part_num):
    sign_var = part_num - 1
    best_cost = (1 - sign_var * 2) * sys.maxsize
    best_gear= []
    
    for w in WEAPONS:
        for a in ARMORS:
            for r1, r2 in itertools.combinations(RINGS, 2):
                sum_gear = tuple(map(sum, zip(w[:-1], a[:-1], r1[:-1], r2[:-1])))
                player = Toon(hp=100, damage=sum_gear[1], armor=sum_gear[2])
                # Using sign_var to negate conditions for part 2, exploiting the fact that bool(positive) = bool(negative) = True and bool(0) = False
                if (sign_var - player_wins(player, boss)) & (sign_var - (sum_gear[0] < best_cost)):
                        best_cost = sum_gear[0]
                        best_gear = w, a, r1, r2
                    
    return best_cost, best_gear
                

if __name__ == "__main__":
    input_file = 'input.txt'
    part_num = 1

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        part_num = int(sys.argv[2])

    boss = read_boss(input_file)
    
    best_cost, best_gear = solve_brute_force(boss, part_num)
    print('The cost is {} for equipping {} with {}, {} on left hand and {} on right hand.'.format(best_cost,
                                                                                                  best_gear[0].name,
                                                                                                  best_gear[1].name,
                                                                                                  best_gear[2].name,
                                                                                                  best_gear[3].name))
