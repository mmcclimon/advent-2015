from collections import namedtuple


class Spell:
    def __init__(self, **kwargs):
        self.cost = kwargs['cost']
        self.name = kwargs['name']
        self.dmg = kwargs.get('damage', 0)
        self.heal = kwargs.get('heal', 0)
        self.length = kwargs.get('length', 0)
        self.armor_effect = kwargs.get('armor_effect', 0)
        self.damage_effect = kwargs.get('damage_effect', 0)
        self.mana_effect = kwargs.get('mana_effect', 0)

    def __repr__(self):
        if self.length > 0:
            return f"<{self.name} @{self.length}>"

        return f"<{self.name}>"

    def clone(self):
        other = type(self)()
        other.length = self.length
        return other


class MagicMissile(Spell):
    def __init__(self):
        super().__init__(name='MagicMissile', cost=53, damage=4)


class Drain(Spell):
    def __init__(self):
        super().__init__(name='Drain', cost=73, damage=2, heal=2)


class Shield(Spell):
    def __init__(self):
        super().__init__(name='Shield', cost=113, length=6, armor_effect=7)


class Poison(Spell):
    def __init__(self):
        super().__init__(name='Poison', cost=173, length=6, damage_effect=3)


class Recharge(Spell):
    def __init__(self):
        super().__init__(name='Recharge', cost=229, length=5, mana_effect=101)


SPELLS = [MagicMissile, Drain, Shield, Poison, Recharge]

Player = namedtuple('Player', ['mana', 'hp', 'effects'])
Boss = namedtuple('Boss', ['hp', 'dmg'])


def play_game(player, boss, hard_mode=False):
    queue = []
    queue.append((player, boss, 1, 0))

    spent_amounts = []
    seen_states = set()

    while len(queue) > 0:
        p, b, turn, total_spent = queue.pop()

        hp = p.hp
        mana = p.mana

        armor = 0
        damage = 0
        effects = []

        if hard_mode:
            hp -= 1

        # process end-of-game conditions
        if hp <= 0:
            # print("oh no, player died.")
            continue

        if b.hp <= 0:
            # print("yay, player won")
            spent_amounts.append(total_spent)
            continue

        # process effects
        for spell in p.effects:
            spell.length -= 1
            mana += spell.mana_effect
            armor += spell.armor_effect
            damage += spell.damage_effect

            if spell.length > 0:
                effects.append(spell)

        # BOSS TURN
        if turn % 2 == 0:
            boss_hp = b.hp - damage

            if boss_hp <= 0:
                # print("yay, player won")
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

        # PLAYER TURN
        if mana < 53:
            # print("player can make no moves, so dies.")
            continue

        # Before adding a bunch of nonsense to the queue: we only need to
        # continue if we haven't been in this exact state before.
        ekey = ';'.join(sorted(map(str, effects)))
        key = (hp, mana, b.hp, ekey, total_spent)
        if key in seen_states:
            continue
        else:
            seen_states.add(key)

        # try everything we can
        have_effects = set(map(lambda e: type(e).__name__, effects))
        for cls in SPELLS:
            if cls.__name__ in have_effects:
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
