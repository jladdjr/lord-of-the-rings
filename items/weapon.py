#!/usr/bin/python
import constants
from items.item import Item

class Weapon(Item):
    """
    A class of weapons.
    """
    
    def __init__(self, damage, name, description, weight):
        """
        Initializes weapon class.

        @param damage:        Damage stat of weapon.
        @param name:          Name of weapon.
        @param description:   Description of weapon.
        @param weight:        Weight of weapon.
        """
        Item.__init__(self, name, description, weight)
        self._damage = damage

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.WEAPON
