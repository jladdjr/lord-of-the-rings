#!/usr/bin/python
import constants
from items.item import Item

class Potion(Item):
    """
    A class of potions.
    """
    
    def __init__(self, name, description, weight, healing):
        """
        Initializes potions class.

        @param name:          Name of portion.
        @param description:   Description of potion.
        @param weight:        Weight of weapon.
        @param healing:       Healing stat of weapon.
        """
        Item.__init__(self, name, description, weight)
        self._healing = healing

    def getHealing(self):
        """
        Returns the potion's healing stat.

        @return: Potion's healing stat.
        """
        return self._healing

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.POTION
