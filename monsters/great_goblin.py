#!/usr/bin/python

from monsters.monster import Monster

class GreatGoblin(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a GreatGoblin monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        self._name = "Great Goblin"
        self._description = "\"Give me ALL of your stuff!\""
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = "slice and diced"
        self._deathString = "Went back home."
