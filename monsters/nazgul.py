#!/usr/bin/python

from monsters.monster import Monster

class Nazgul(Monster):
    """
    A generic monster to be used as a parent for specific future monster classes.
    """
    def __init__(self, hp, attack, experience):
        """
        Initializes a Nazgul monster. Inherits from Monster.

        @param hp:             Hit points of monster.
        @param attack:         Attack stat of monster.
        @param experience:     Experienced gained for defeating monster.
        """
        if hp < 1 or attack < 1 or experience < 1:
            errorMsg = "Invalid base stats for monster; stats must be positive integers."
            raise AssertionError(errorMsg)

        self._name = "Nazgul"
        self._description = "Masked riders and servants of Sauron."
        self._hp = hp
        self._attack = attack
        self._experience = experience
        self._attackString = "Cleaved at you"
        self._deathString = "Ran off!"
        
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

    def getHp(self):
        """
        Get monster's HP.
        
        @return: Monster's HP.
        """
        return self._hp
    
    def attack(self, target):
        """
        Simulates attacking a given target.

        @param target:      Target to attack.
        """
        target.takeAttack(self._attack)

    def getAttack(self):
        """
        Get monster's attack.
        
        @return: Monster's attack.
        """
        return self._attack
        
    def takeAttack(self, attack): 
        """
        Simulates taking an attack.
        Hp is floored at zero.

        @param attack:      Amount of attack taken.
        """
        self._hp = max(self._hp - attack, 0)
        
    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster's experience.
        """
        return self._experience

    def getAttackString(self):
        """
        Gets monster's attack string.

        @return: Monster's attack string.
        """
        return self._attackString

    def getdeathString(self):
        """
        Gets monster's death string.

        @return: Monster's death string.
        """
        return self._deathString
