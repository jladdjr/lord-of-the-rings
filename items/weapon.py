#!/usr/bin/python
from constants import ItemType 
from items.item import Item

class Weapon(Item):
    """
    A class of weapons.
    """
    def __init__(self, name, description, weight, attack):
        """
        Initializes weapon class.

        @param name:          Name of weapon.
        @param description:   Description of weapon.
        @param weight:        Weight of weapon.
        @param attack:        Attack stat of weapon.
        """
        Item.__init__(self, name, description, weight)
        self._attack = attack

    def getAttack(self):
        """
        Returns the weapon's attack stat.

        @return: Weapon's attack.
        """
        return self._attack

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.WEAPON
