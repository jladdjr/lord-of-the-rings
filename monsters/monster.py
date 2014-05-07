#!/usr/bin/python

class Monster(object):
    """
    A generic monster to be used as a parent for specific future monster classes.
    """
    def __init__(self, name, description, hp, attack, experience):
        """
        Initializes an item object.

        @param name:        Name of monster.
        @param description: Description of monster.
        @param hp:          Hit points of monster.
        @param attack:      Attack stat of monster.
        @param experience:  Experienced gained for defeating monster.
        """
        if (not name) or (not description) or (not hp) or \
            (not attack) or (not experience):
            raise AssertionError("Monster must have name, description, hp, attack, and experience.")
        if hp < 1 or attack < 1 or experience < 1:
            errorMsg = "Invalid base stats for monster; stats must be positive integers."
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self._hp = hp
        self._attack = attack
        self._experience = experience

    def attack(self, target):
        """
        Simulates attacking a given target.

        @param target:      Target to attack.
        """
        target.takeAttack(self._attack)
        
    def takeAttack(self, attack): 
        """
        Simulates taking an attack.
        Hp is floored at zero.

        @param attack:      Amount of attack taken.
        """
        self._hp = max(self._hp - attack, 0)

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
        
    def getAttack(self):
        """
        Get monster's attack.
        
        @return: Monster's attack.
        """
        return self._attack

    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster's experience.
        """
        return self._experience
