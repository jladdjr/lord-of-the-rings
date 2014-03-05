#!/usr/bin/python

class Stats(object):
    """
    Returns character stats given character level.
    """

    def __init__(self, level):
        """
        Determines stats dependent on level.

        @level:   The level of any given character.
        """
        self._level = level

        self._hp = self._level * constants.HP_STAT
        self._damage = self._level * constants.DAMAGE_STAT

    def getStats(self):
        """
        Returns character stats.

        @return:   Return's a specific character's stats
        """
        return self._hp, self._damage
