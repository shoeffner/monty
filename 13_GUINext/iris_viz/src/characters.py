class Character:
    """A strong character to fight for the crown!"""

    def __init__(self, health=1000, strength=75, title='Knight', name='Roy'):
        self.health = health
        self.strength = strength
        self.title = title
        self.name = name

    def weak_attack(self):
        """Returns the damage of a weak attack.

        A weak attack is calculated with 0.8 * strength.
        """
        return self.strength * 0.8

    def strong_attack(self):
        """Returns the damage of a strong attack.

        A strong attack is calculated with 1.5 * strength.
        """
        return self.strength * 1.5

    def alive(self):
        """Check if the character is alive.

        Returns:
            If the character's health is > 0, this returns True. Else False.
        """
        return self.health > 0

    def damage(self, damage):
        """Reduces the health by damage."""
        self.health -= damage

    def __str__(self):
        return '{} {}'.format(self.title, self.name)
