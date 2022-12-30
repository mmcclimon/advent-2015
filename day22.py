from collections import namedtuple


class MagicMissile:
    def __init__(self):
        self.cost = 53
        self.dmg = 4
        self.heal = 0
        self.length = 0
        self.action = {}

    def __repr__(self):
        return "<MagicMissile>"


class Drain:
    def __init__(self):
        self.cost = 73
        self.dmg = 2
        self.heal = 2
        self.length = 0
        self.action = {}

    def __repr__(self):
        return "<Drain>"


class Shield:
    def __init__(self):
        self.cost = 113
        self.dmg = 0
        self.heal = 0
        self.length = 6
        self.action = {'armor': 7}

    def __repr__(self):
        return f"<Shield @{self.length}>"

    def clone(self):
        other = Shield()
        other.length = self.length
        return other


class Poison:
    def __init__(self):
        self.cost = 173
        self.dmg = 0
        self.heal = 0
        self.length = 6
        self.action = {'damage': 3}

    def __repr__(self):
        return f"<Poison @{self.length}>"

    def clone(self):
        other = Poison()
        other.length = self.length
        return other


class Recharge:
    def __init__(self):
        self.cost = 229
        self.dmg = 0
        self.heal = 0
        self.length = 5
        self.action = {'mana': 101}

    def __repr__(self):
        return f"<Recharge @{self.length}>"

    def clone(self):
        other = Recharge()
        other.length = self.length
        return other


SPELLS = [MagicMissile, Drain, Shield, Poison, Recharge]

Player = namedtuple('Player', ['mana', 'hp', 'effects'])
Boss = namedtuple('Boss', ['hp', 'dmg'])


def play_game(player, boss, hard_mode=False):
    queue = []
    queue.append((player, boss, 1, 0))

    spent_amounts = []
    seen_states = set()
    completed = 0

    while len(queue) > 0:
        p, b, turn, total_spent = queue.pop()

        hp = p.hp
        mana = p.mana

        armor = 0
        damage = 0
        effects = []

        if hard_mode:
            hp -= 1

        # if completed % 10000 == 0:
        #     print(f"completed {completed} games (queue = {len(queue)})")

        # process end-of-game conditions
        if hp <= 0:
            completed += 1
            # print("oh no, player died.")
            continue

        if b.hp <= 0:
            # print("yay, player won")
            completed += 1
            spent_amounts.append(total_spent)
            continue

        # process effects
        for spell in p.effects:
            spell.length -= 1
            if 'mana' in spell.action:
                mana += spell.action['mana']
            if 'armor' in spell.action:
                armor += spell.action['armor']
            if 'damage' in spell.action:
                damage += spell.action['damage']

            if spell.length > 0:
                effects.append(spell)

        if turn % 2 == 0:
            # boss turn
            boss_hp = b.hp - damage

            if boss_hp <= 0:
                # print("yay, player won")
                completed += 1
                spent_amounts.append(total_spent)
                continue

            hp = hp - max(b.dmg - armor, 1)
            queue.append((
                Player(mana=mana, hp=hp, effects=effects),
                Boss(hp=boss_hp, dmg=b.dmg),
                turn + 1,
                total_spent,
                ))

            continue

        # it's now the player turn
        if mana < 53:
            # print("player can make no moves, so dies.")
            completed += 1
            continue

        # prune if we've seen this state already
        ekey = ';'.join(sorted(map(str, effects)))
        key = (hp, mana, b.hp, ekey, total_spent)
        if key in seen_states:
            continue

        seen_states.add(key)

        # try everything we can
        have = set(map(lambda e: type(e).__name__, effects))
        for cls in SPELLS:
            if cls.__name__ in have:
                continue

            spell = cls()
            if mana < spell.cost:
                continue

            this_effects = []
            for eff in effects:
                this_effects.append(eff.clone())

            this_mana = mana - spell.cost
            this_hp = hp + spell.heal
            boss_hp = b.hp - (damage + spell.dmg)

            if spell.length > 0:
                this_effects.append(spell)

            queue.append((
                Player(mana=this_mana, hp=this_hp, effects=this_effects),
                Boss(hp=boss_hp, dmg=b.dmg),
                turn + 1,
                total_spent + spell.cost
                ))

    return min(spent_amounts)


# player = Player(hp=10, mana=250, effects=[])
# boss = Boss(hp=14, dmg=8)
player = Player(hp=50, mana=500, effects=[])
boss = Boss(hp=58, dmg=9)

part1 = play_game(player, boss)
print(f"part 1: {part1}")

part2 = play_game(player, boss, True)
print(f"part 2: {part2}")
