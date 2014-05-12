#!/usr/bin/python

from monsters.monster import Monster

class Troll(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Troll monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        self._name = "Troll"
        self._description = "\"Merrily I troll along.\""
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = "slams you with fists of malice"
        self._deathString = "\"Merrily I troll away.\""
