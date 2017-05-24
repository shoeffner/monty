class Knight:

    def __init__(self, level=31, strength=20, magic=20, defense=30, agility=7):
        """Instantiates a knight with its default attributes.

        Args:
            level: Defaults to 31.
            strength: Defaults to 20.
            magic: Defaults to 20.
            defense: Defaults to 30.
            agility: Defaults to 7.
        """
        self.level = level
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.agility = agility
        self.health = self.maximum_health()

    def maximum_health(self):
        """Returns the maximum health of this knight."""
        return 69 + 3 * self.level + 28 * self.defense

    def is_alive(self):
        """Returns true if this knight is alive."""
        return self.health > 0

    def normal_attack(self, other):
        """Calculates the attack damage with a normal attack and lets other
        take damage accordingly.

        Args:
            other: The attack target.
        """
        damage = (3 + self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def strong_attack(self, other):
        """Calculates the attack damage with a strong attack and lets other
        take damage accordingly.

        Args:
            other: The attack target.
        """
        damage = (5 + 1.15 * self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def throw_attack(self, other):
        """Calculates the attack damage with a throw attack and lets other
        take damage accordingly.

        Args:
            other: The attack target.
        """
        damage = (10 + 1.2 * self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def arrow_attack(self, other):
        """Calculates the attack damage with an arrow attack and lets other
        take damage accordingly.

        Args:
            other: The attack target.
        """
        damage = 2 + self.agility
        other.take_damage(damage)

    def take_damage(self, attack_damage):
        """Reduces the health by the defense modified attack_damage.

        Args:
            attack_damage: The attack damage.
        """
        self.health -= (attack_damage * (1.2 - 0.01 * self.defense) + 0.5) // 1


if __name__ == '__main__':
    red = Knight(level=32, strength=32)
    blue = Knight()

    # This creates lists of functions!
    red_combo = [Knight.strong_attack] * 2 + [Knight.normal_attack]
    blue_combo = [Knight.normal_attack] * 3 + [Knight.throw_attack]

    # The dashing blue knight attacks twice with his arrow before the battle
    # starts...
    blue.arrow_attack(red)
    blue.arrow_attack(red)

    # Each round consists of red attacking (odd half_rounds) and blue attacking
    # (even half_rounds). An attack goes through the respective combo and calls
    # each attacks therein with the attacker as self and the attacked as other.
    half_round = 1
    while red.is_alive() and blue.is_alive():
        for attack in red_combo if half_round & 1 else blue_combo:
            # The * unpacks. Calling attack(*[red, blue]) is equivalent to
            # attack(red, blue).
            # As this was hard to read, especially with the [::1] or [::-1],
            # we changed this to a more readable version (which is probably
            # better anyways:
            if half_round & 1:
                attack(red, blue)
            else:
                attack(blue, red)
            # Original:
            # attack(*([red, blue][::1 if half_round & 1 else -1]))
        half_round += 1

    print('Round:', half_round // 2)
    print('Red alive?', red.is_alive(), 'HP:', red.health)
    print('Blue alive?', blue.is_alive(), 'HP:', blue.health)
