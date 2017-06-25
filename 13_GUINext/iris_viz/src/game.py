class Game:
    """A knightly tournament."""

    def __init__(self, player, npc):
        """Initializes a game.

        Sets the counter to 0.

        Args:
            player: The player character.
            npc: The non-player character.
        """
        self.player = player
        self.npc = npc
        self.round = 0

    def fight(self, player_attack, npc_attack):
        """Lets two characters fight.

        Each attack can be 'w' or 's' to denote a weak or a strong attack.
        Each character deals the damage calculated by their respective weak or
        strong attacks.

        Args:
            player_attack: The player's attack, 'w' or 's'.
            npc_attack: The npc's attack, 'w' or 's'.

        Returns:
            A round report.
        """
        self.round += 1
        attacks = {'w': lambda who: who.weak_attack(),
                   's': lambda who: who.strong_attack()}
        self.npc.damage(attacks[player_attack](self.player))
        self.player.damage(attacks[npc_attack](self.npc))

        report = ['\nRound {}:'.format(self.round)]
        for c, a in zip([self.player, self.npc], [player_attack, npc_attack]):
            report.append('{} attacks with a {} attack.'
                          .format(c, 'weak' if a == 'w' else 'strong'))
        return '\n'.join(report)

    def active(self):
        """Returns True if both characters are alive."""
        return self.player.alive() and self.npc.alive()

    def result(self):
        """Returns some detailed battle report."""
        result = []
        if not self.player.alive():
            result.append('You died!')
        if not self.npc.alive():
            result.append('{} died!'.format(self.npc.name))
        result.append('The noble challengers fought well.')
        result.append('(Rounds: {})'.format(self.round))
        return '\n'.join(result)
