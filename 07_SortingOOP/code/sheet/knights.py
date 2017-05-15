# TODO: Add the class Knight:
class Knight:
    pass


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
