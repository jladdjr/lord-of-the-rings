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
        Monster.__init__(self, "Great Goblin", "\"Give me ALL of your stuff!\"", stats, "slice and diced", "\"I'm going back home too.\"")       
