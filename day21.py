import itertools

# price: (dmg, armor)
weapons = {
    8:  (4, 0),  # dagger
    10: (5, 0),  # shortsword
    25: (6, 0),  # warhammer
    40: (7, 0),  # longsword
    74: (8, 0),  # greataxe
}

armors = {
    0:   (0, 0),  # nothin, yo
    13:  (0, 1),  # leather
    31:  (0, 2),  # chain
    53:  (0, 3),  # splint
    75:  (0, 4),  # banded
    102: (0, 5),  # plate
}

rings = {
    0:   (0, 0),    # nothin, yo
    25:  (1, 0),    # damage 1
    50:  (2, 0),    # damage 2
    100: (3, 0),    # damage 3
    20:  (0, 1),    # def 1
    40:  (0, 2),    # def 2
    80:  (0, 3),    # def 3
}


class Combatant:
    def __init__(self, name, hp, dmg, armor):
        self.name = name
        self.hp = hp
        self.damage = dmg
        self.armor = armor

    def hit(self, other):
        damage = (self.damage - other.armor)
        other.hp -= max(damage, 1)

    def is_dead(self):
        return self.hp <= 0

def player_wins_sim(player, boss):
    for turn in itertools.cycle([(player, boss), (boss, player)]):
        attacker, victim = turn
        attacker.hit(victim)
        if victim.is_dead():
            return attacker == player

    raise RuntimeError('unreachable!')


best = None
worst = None
bossargs = ['boss', 100, 8, 2]

for wcost, wtup in weapons.items():
    for acost, atup in armors.items():
        all_rings = itertools.chain(rings.items(), [(0, (0, 0))])

        for ring1, ring2 in itertools.combinations(all_rings, 2):
            cost = wcost + acost + ring1[0] + ring2[0]
            damage = wtup[0] + ring1[1][0] + ring2[1][0]
            armor = atup[1] + ring1[1][1] + ring2[1][1]

            boss = Combatant(*bossargs)
            player = Combatant('player', 100, damage, armor)

            if player_wins_sim(player, boss):
                if not best or best > cost:
                    best = cost
            else:
                if not worst or worst < cost:
                    worst = cost


print(f'part 1: {best}')
print(f'part 2: {worst}')
