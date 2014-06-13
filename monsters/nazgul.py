#!/usr/bin/python

from monsters.monster import Monster

class Nazgul(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Nazgul monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, "Nazgul", "\"AAAAEEEEEEEEEEE!!!\"", stats, "cleaved at you", "\"AAAAEEEEEEEEEEE!!!\"")
