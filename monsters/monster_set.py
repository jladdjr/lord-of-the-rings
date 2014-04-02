#!/usr/bin/python

from monster import Monster

#TODO: Perhaps we want a more generic Party() class that could be used
#      for a collection of monsters or players/teammates. -JDL

class MonsterSet(object):
    """
    A simple collection of monsters.
    """

    def __init__(self, monsterSet=None):
        """
        Initialize a Monsters object.

        @keyword monsterSet:     (Optional) A single Monster object or a
                                 list of Monster objects.
        """
        self._monsters = []

        #Received single monster
        if isinstance(monsterSet, Monster):
            self._monsters.append(monsterSet)
            self._experience += monsterSet.getExperience()
        #Received set of monsters
        elif isinstance(monsterSet, list):
            for monster in monsterSet:
                if not isinstance(monster, Monster):
                    errorMsg = "Monsters initialized with list containing non-Monster object(s)."
                    raise AssertionError(errorMsg)
                self._monsters.append(monster)
                self._experience += monster.getExperience()

    def addMonster(self, monster):
        """
        Adds an monster.

        @param monster:    A monster.
        """
        #Check preconditions
        if not isinstance(monster, Monster):
            errorMsg = "Monsters.addMonster() passed non-Monster object."
            raise AssertionError(errorMsg)

        self._monsters.append(monster)
        self._experience += monster.getExperience()

    def removeMonster(self, monster):
        """
        Removes an monster.

        @param monster:    An monster in this collection.
        """
        self._monsters.remove(monster)
        self._experience -= monster.getExperience()
   
    def containsMonster(self, monster):
        """
        Determines if monster is contained in this collection.

        @param monster:    An monster.
        @return:        True if monster is in this collection, False otherwise.
        """
        return (monster in self._monsters)

    def count(self):
        """
        Returns the number of monsters.

        @return:    Number of monsters.
        """
        return len(self._monsters)

    def experience(self):
        """
        Determines total experience of monsters.

        @return: Total experience of monsters.
        """
        return self._experience 
 
    def __iter__(self):
        """
        Provide an iterator for this set of monsters.


        Allows you to create for loops using Monsters objects:


            >>> from monster import Monster
            >>> from monster_set import MonsterSets
            >>> monster1 = Monster("sword", "made by elves", 2)
            >>> monster2 = Monster("helmet", "made by men", 1)
            >>> monster3 = Monster("healing potion", "restores health", 1)
            >>> myMonsters = Monsters([monster1, monster2, monster3])
            >>> for monster in myMonsters:
            ...     print monster.getName()
            ... 
            sword
            helmet
            healing potion


        """
        return iter(self._monsters)
