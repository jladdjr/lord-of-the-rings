#!/usr/bin/python

#TODO: Move this back into player (e.g. createa getHp() method in player).

class Stats(object):
    """
    Returns character stats given character level.
    """
    def __init__(self, level):
        """
        Determines stats dependent on level.

        @player:  The character in focus (for example: Frodo).
        @level:   The level of any given character.
        """
        self._level = level
        self._hp = self._level * constants.HP_STAT
        self._damage = self._level * constants.DAMAGE_STAT

    def getStats(self, level):
        """
        Returns character stats.
        
        @level:    Return the stats of character given level.
        @return:   Return's a specific character's stats.
        """
        self._level = level
        self._hp = self._level * constants.HP_STAT
        self._damage = self._level * constants.DAMAGE_STAT
        
        self._stats = [self._hp, self._damage]
        return self._stats
