#!/usr/bin/python

from constants import ItemType
from items.item import Item

class Charm(Item):
    """
    Charm class. Charm inherits from Item and can modify any number of player attributes.
    """
    def __init__(self, name, description, weight, attack, defense, hp, cost):
        """
        Initializes charm class.

        @param name:         The name of the item.
        @param description:  Charm description.
        @param weight:       Charm weight.
        @param attack:       Attack bonus given by charm.    
        @param defense:      The defense stat of the charm. Reduces the amount
                             of damage that player receives by this amount.
        @param hp:           The hp bonus of the charm. 
        """
        Item.__init__(self, name, description, weight)
        self._attack = attack
        self._defense = defense
        self._hp = hp
        self._cost = cost
        
    def getAttack(self):
        """
        Returns the charm's attack stat bonus.

        @return:    Charm's attack bonus.
        """
        return self._attack
        
    def getDefense(self):
        """
        Returns the charm's defense stat bonus.

        @return:    Charm's defense bonus.
        """
        return self._defense
    
    def getHp(self):
        """
        Returns the charm's hp bonus.

        @return:    Charm's hp bonus.
        """
        return self._hp
        
    def getCost(self):
        """
        Returns charm cost.

        @return:    Charm's cost stat.
        """
        return self._cost

    def getType(self):
        """
        Returns the item's type.

        @return:   Item's type.
        """
        return ItemType.charm