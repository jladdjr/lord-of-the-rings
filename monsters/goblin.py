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
        Monster.__init__(self, "Goblin", "\"Give me all of your stuff!\"", stats, "slice and diced", "\"I'm going back home.\"") 
