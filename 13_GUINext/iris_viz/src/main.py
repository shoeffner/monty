import random

import characters
import game


def main():
    choice = '0'
    while choice not in 'kpq':
        choice = input('Knight or Princess? [k/p] ')
    if choice == 'q':
        print('Maybe you are braver next time!')
        return

    character = characters.Character(1000, 75, 'Knight', 'Roy')
    enemy = characters.Character(800, 100, 'Princess', 'Lisi')
    if choice == 'p':
        character, enemy = enemy, character

    print('You are {}. Your opponent is {}.'.format(character, enemy))
    print('Are you ready to take the crown? Fight!')

    fight = game.Game(character, enemy)
    while fight.active():
        attack = 'n'
        while attack not in 'ws':
            attack = input('\nWeak or Strong attack? [w/s] ')
        print(fight.fight(attack, random.choice('ws')))

    print(fight.result())


if __name__ == '__main__':
    main()
