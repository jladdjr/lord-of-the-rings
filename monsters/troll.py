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
        Monster.__init__(self, "Troll", "\"Merrily I troll along.\"", stats, "slams you with fists of malice", "\"Merrily I troll away.\"") 
