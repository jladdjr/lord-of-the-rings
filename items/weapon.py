#!/usr/bin/python

from constants import ItemType 
from items.item import Item

class Weapon(Item):
    """
    A child class of Item.
    
    Weapon serves as the offensive item class of the game. Weapon 
    has the defining parameter, attack, which adds to player attack 
    to constitute player damage.
    """
    def __init__(self, name, description, weight, cost, attack):
        """
        Initializes weapon class.

        @param name:          Name of weapon.
        @param description:   Description of weapon.
        @param weight:        Weight of weapon.
        @param cost:          The cost of the weapon.
        @param attack:        Attack stat of weapon. Player damage increases by this
                              amount when weapon is equipped.
        """
        Item.__init__(self, name, description, weight, cost)
        
        self._attack = attack
    
    def getAttack(self):
        """
        Returns weapon attack stat.

        @return:    Weapon attack stat.
        """
        return self._attack

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.WEAPON