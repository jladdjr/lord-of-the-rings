#!/usr/bin/python
import constants
from items.item import Item

class Weapon(Item):
    """
    A class of weapons.
    """
    
    def __init__(self, name, description, weight, damage):
        """
        Initializes weapon class.

        @param name:          Name of weapon.
        @param description:   Description of weapon.
        @param weight:        Weight of weapon.
        @param damage:        Damage stat of weapon.
        """
        Item.__init__(self, name, description, weight)
        self._damage = damage

    def getDamage(self):
        """
        Returns the weapon's damage stat.

        @return: Weapon's damage.
        """
        return self._damage

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.WEAPON
