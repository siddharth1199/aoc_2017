from itertools import combinations

WEAPONS = [
	[8, 4, 0],
	[10, 5, 0],
	[25, 6, 0], 
	[40, 7, 0],
	[74, 8, 0]
]

ARMOR = [
	[13, 0, 1],
	[31, 0, 2],
	[53, 0, 3],
	[75, 0, 4],
	[102, 0, 5],
	[0, 0, 0]
]

RINGS = [
	[25, 1, 0],
	[50, 2, 0],
	[100, 3, 0],
	[20, 0, 1],
	[40, 0, 2],
	[80, 0, 3],
	[0, 0, 0],
	[0, 0, 0]
]
PLAYER_HIT_POINTS = 100

def parse_input(path = 'input.txt'):
	boss_stats = {}
	with open(path) as f:
		for line in f:
			stats, val = line.split(':')
			boss_stats[stats] = int(val.strip())
	return boss_stats['Hit Points'], boss_stats['Damage'], boss_stats['Armor']

def generate_equip_combo():
	for i in range(len(WEAPONS)):
		for j in range(len(ARMOR)):
			for r1, r2 in combinations(range(len(RINGS)), 2):
				yield (i, j, r1, r2)

def get_stats(equip_combo):
	weapon, armor, ring1, ring2 = equip_combo
	cost = WEAPONS[weapon][0] + ARMOR[armor][0] + RINGS[ring1][0] + RINGS[ring2][0]
	damage = WEAPONS[weapon][1] + ARMOR[armor][1] + RINGS[ring1][1] + RINGS[ring2][1]
	armor = WEAPONS[weapon][2] + ARMOR[armor][2] + RINGS[ring1][2] + RINGS[ring2][2]
	return cost, damage, armor


def simulation(player_damage, player_armor, boss_hit_points, boss_damage, boss_armor):
	damage_player_deals = max(1, player_damage - boss_armor)
	damage_boss_deals = max(1, boss_damage - player_armor)

	if PLAYER_HIT_POINTS % damage_boss_deals == 0:
		player_max_rounds = PLAYER_HIT_POINTS / damage_boss_deals
	else:
		player_max_rounds = PLAYER_HIT_POINTS // damage_boss_deals + 1

	if boss_hit_points % damage_player_deals == 0:
		boss_max_rounds = boss_hit_points / damage_player_deals
	else:
		boss_max_rounds = boss_hit_points // damage_player_deals + 1
	
	return player_max_rounds, boss_max_rounds	


def main():
	min_cost = float('inf')
	max_cost = float('-inf')
	boss_hit_points, boss_damage, boss_armor = parse_input()

	equip_combo_iter = generate_equip_combo()
	for equip_combo in equip_combo_iter:
		cost, damage, armor = get_stats(equip_combo)
		player_max_rounds, boss_max_round = simulation(damage, armor, boss_hit_points, boss_damage, boss_armor)
		if player_max_rounds >= boss_max_round:
			min_cost = min(min_cost, cost)
		else:
			max_cost = max(max_cost, cost)
	return min_cost, max_cost


if __name__ == '__main__':
	answer1, answer2 = main()
	print(answer1, answer2)	
