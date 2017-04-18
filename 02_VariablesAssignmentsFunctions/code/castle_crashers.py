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


def red_combo_damage(lvl_red, str_red, def_blue):
    strong_damage = damage_taken(strong_attack_damage(lvl_red, str_red),
                                 def_blue)
    normal_damage = damage_taken(normal_attack_damage(lvl_red, str_red),
                                 def_blue)
    return 2 * strong_damage + normal_damage


def blue_combo_damage(lvl_blue, str_blue, def_red):
    normal_damage = damage_taken(normal_attack_damage(lvl_blue, str_blue),
                                 def_red)
    throw_damage = damage_taken(throw_attack_damage(lvl_blue, str_blue),
                                def_red)
    return 3 * normal_damage + throw_damage


def fight(lvl_red, str_red, def_red, hp_perc_red,
          lvl_blue, str_blue, def_blue, hp_perc_blue):
    health_red = round(hp_perc_red / 100 * maximum_health(lvl_red, def_red))
    health_blue = round(hp_perc_blue / 100 * maximum_health(lvl_blue, def_blue))

    loss_blue = red_combo_damage(lvl_red, str_red, def_blue)
    loss_red = blue_combo_damage(lvl_blue, str_blue, def_red)

    rounds_to_kill_red = math.ceil(health_red / loss_red)
    rounds_to_kill_blue = math.ceil(health_blue / loss_blue)

    print('It takes red', rounds_to_kill_blue, 'rounds to kill blue.')
    print('It takes blue', rounds_to_kill_red, 'rounds to kill red.')

    if rounds_to_kill_red < rounds_to_kill_blue:
        print('Blue wins!')
    else:
        print('Red wins!')


level_red = 31
strength_red = 20
defense_red = 30
start_health_perc_red = 25

level_blue = 31
strength_blue = 20
defense_blue = 30
start_health_perc_blue = 20

fight(level_red, strength_red, defense_red, start_health_perc_red,
      level_blue, strength_blue, defense_blue, start_health_perc_blue)
