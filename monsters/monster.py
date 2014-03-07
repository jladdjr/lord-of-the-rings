#!/usr/bin/python

class Monster(object):
    """
    A generic monster to be used as a parent for specific future monster classes.
    """

    def __init__(self, name, description, hp, damage, experience):
        """
        Initializes an item object.

        @param name:        Name of monster.
        @param description: Description of monster.
        @param hp:          Hit points of monster.
        @param damage:      Damage stat of monster.
        @param experience:  Experienced gained for defeating monster.
        """
        if (not name) or (not description) or (not hp) or \
            (not damage) or (not experience):
            raise AssertionError("Monster must have name, description, hp, damage, and experience.")
        if hp < 1 or damage < 1 or experience < 1:
            errorMsg = "Invalid base stats for monster; stats must be positive integers."
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self._hp = hp
        self._damage = damage
        self.experience = experience

    def attack(self, target):
        """
        Simulates attacking a given target.

        @param target:      Target to attack.
        """
        target.takeDamage(self._damage)

        #TODO: Probably want BattleEngine to be responsible for 
        #reporting battle events.
        print "%s attacked %s for %s damage!" %(self._name, target, self._damage)
        
    def takeDamage(self, damage): 
        """
        Simulates taking damage from attack.

        @param damage:      Amount of damage taken.
        """
        self._hp -= damage
        print "%s took %s damage!" %(self._name, damage)

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
        
    def getDamage(self):
        """
        Get monster's damage.
        
        @return: Monster's damage.
        """
        return self._damage

    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster's experience.
        """
        return self._experience
