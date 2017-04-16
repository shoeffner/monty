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
    return (attack_damage * (1.2 - 0.01 * defense) + 0.5) // 1


# the attributes of our knights
level = 31
strength = 20
magic = 20
defense = 30
agility = 7

# initializing health values
red_health = 0.25 * maximum_health(level, defense)
blue_health = 0.2 * maximum_health(level, defense)

round_counter = 0

# now: FIGHT! until red_health or blue_health are below 0
while red_health > 0 and blue_health > 0:
    # next round!
    round_counter = round_counter + 1

    # red attacks and blue takes damage
    damage_taken_blue = 2 * damage_taken(strong_attack_damage(level, strength), defense) \
                          + damage_taken(normal_attack_damage(level, strength), defense)
    blue_health = blue_health - damage_taken_blue
    print('Round: ', round_counter, ' Blue health: ', blue_health)

    # blue attacks and red takes damage
    damage_taken_red = 3 * damage_taken(normal_attack_damage(level, strength), defense) \
                         + damage_taken(throw_attack_damage(level, strength), defense)
    red_health = red_health - damage_taken_red
    print('Round: ', round_counter, ' Red health: ', red_health)

if blue_health < 0:
    print('Blue goes down first! Red wins!')
else:
    print('Red goes down first! Blue wins')
