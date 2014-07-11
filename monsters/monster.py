#!/usr/bin/python

class Monster(object):
    """
    A generic monster to be used as a parent for specific future monster 
    classes.
    """
    def __init__(self, name, description, stats, attackString, deathString):
        """
        Initializes a monster object.

        @param name:          Name of monster.
        @param description:   Description of monster.
        @param stats:         3-element list of Monster stats including 
                              attack, hp, and experience (in that order).
        @param attackString:  The string displayed with an monster attack. For 
                              instance, Miles "got really pissed and started 
                              charging around."
        @param deathString:   The string displayed with monster death. For 
                              instance, "Miles decided that he's had enough 
                              and went back home."
        """
        self._name = name
        self._description = description
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = attackString
        self._deathString = deathString
        
    def getName(self):
        """
        Gets monster name.

        @return: Monster name.
        """
        return self._name
    
    def getDescription(self):
        """
        Gets monster's description.

        @return: Monster description.
        """
        return self._description

    def getHp(self):
        """
        Get monster's HP.
        
        @return: Monster HP.
        """
        return self._hp
    
    def attack(self, target):
        """
        Simulates attacking a given target.

        @param target: Target to attack.
        """
        target.takeAttack(self._attack)

    def getAttack(self):
        """
        Get monster's attack.
        
        @return: Monster attack.
        """
        return self._attack
        
    def takeAttack(self, attack): 
        """
        Simulates taking an attack.
        HP cannot be less than zero.

        @param attack: Amount of attack taken.
        """
        self._hp = max(self._hp - attack, 0)
        
    def getExperience(self):
        """
        Gets monster's experience.

        @return: Monster experience.
        """
        return self._experience

    def getAttackString(self):
        """
        Gets monster's attack string.

        @return: Monster attack string.
        """
        return self._attackString

    def getDeathString(self):
        """
        Gets monster's death string.

        @return: Monster death string.
        """
        return self._deathString