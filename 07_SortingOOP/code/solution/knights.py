class Knight:

    def __init__(self, level=31, strength=20, magic=20, defense=30, agility=7):
        self.level = level
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.agility = agility
        self.health = self.maximum_health()

    def maximum_health(self):
        return 69 + 3 * self.level + 28 * self.defense

    def is_alive(self):
        return self.health > 0

    def normal_attack(self, other):
        damage = (3 + self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def strong_attack(self, other):
        damage = (5 + 1.15 * self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def throw_attack(self, other):
        damage = (10 + 1.2 * self.strength + 0.1 * self.level) // 1
        other.take_damage(damage)

    def arrow_attack(self, other):
        damage = 2 + self.agility
        other.take_damage(damage)

    def take_damage(self, attack_damage):
        self.health -= (attack_damage * (1.2 - 0.01 * self.defense) + 0.5) // 1


if __name__ == '__main__':
    red = Knight(level=32, strength=32)
    blue = Knight()

    red_combo = [Knight.strong_attack] * 2 + [Knight.normal_attack]
    blue_combo = [Knight.normal_attack] * 3 + [Knight.throw_attack]

    # The dashing blue knight attacks twice with his arrow before the battle
    # starts...
    blue.arrow_attack(red)
    blue.arrow_attack(red)

    half_round = 1
    while red.is_alive() and blue.is_alive():
        for attack in red_combo if half_round & 1 else blue_combo:
            attack(*([red, blue][::1 if half_round & 1 else -1]))
        half_round += 1

    print('Round:', half_round // 2)
    print('Red alive?', red.is_alive(), 'HP:', red.health)
    print('Blue alive?', blue.is_alive(), 'HP:', blue.health)
