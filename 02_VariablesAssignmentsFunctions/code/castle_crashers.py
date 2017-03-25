import math


def strong_attack_damage(level, strength):
    return (5 + 1.15 * strength + 0.1 * level) // 1


def normal_attack_damage(level, strength):
    return (3 + strength + 0.1 * level) // 1


def throw_attack_damage(level, strength):
    return (10 + 1.2 * strength + 0.1 * level) // 1


def maximum_health(level, defense):
    return 69 + 3 * level + 28 * defense


def arrow_damage(agility):
    return 2 + agility


def damage_taken(attack_damage, defense):
    return round(attack_damage * (1.2 - 0.01 * defense))


level = 31
strength = 20
defense = 20
magic = 20
agility = 7
red_knight_health = 0.25 * maximum_health(level, defense)
blue_knight_health = 0.2 * maximum_health(level, defense)

red_attack_damage = 2 * strong_attack_damage(level, strength) \
                  + 1 * normal_attack_damage(level, strength)
blue_attack_damage = 3 * normal_attack_damage(level, strength) \
                   + 1 * throw_attack_damage(level, strength)

red_health_loss = damage_taken(blue_attack_damage, defense)
blue_health_loss = damage_taken(red_attack_damage, defense)

rounds_to_kill_red = math.ceil(red_knight_health / red_health_loss)
rounds_to_kill_blue = math.ceil(blue_knight_health / blue_health_loss)

print('It takes red', rounds_to_kill_blue, 'rounds to kill blue.')
print('It takes blue', rounds_to_kill_red, 'rounds to kill red.')

if rounds_to_kill_red < rounds_to_kill_blue:
    print('Blue wins!')
else:
    print('Red wins!')
