#!/usr/bin/python

from monsters.monster import Monster

class Goblin(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Goblin monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        self._name = "Goblin"
        self._description = "\"Give me all of your stuff!\""
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = "slice and diced"
        self._deathString = "Went back home."
