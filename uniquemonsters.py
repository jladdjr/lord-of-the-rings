#!/usr/bin/python

from monster import Monster

class Nazgul(Monster):
    """
    A Nazgûl monster.
    """

    def __init__(self, name, description, player):
        """
        Initializes the Nazgûl. Nazgûl is a monster that player fights throughout the game
        and whose difficulty is dependent on player level.

        @param name:        Name of monster
        @param description: Description of monster.
        @param experience:  Experienced gained for defeating monster.
        @param player:      Player stats are used for deteremining Nazgûl difficulty.
        """
        Monster.__init__(self, name, description, experience)

    def getName(self):
        """
        Gets monster name.

        @return: Monster's name.
        """
        return self._name

    def getDescription(self):
        """
        Gets monster's description.

        @return: Monster's description.
        """
        return self._description

    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster's experience.
        """
        return self._experience
