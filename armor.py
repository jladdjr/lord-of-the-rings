#!/usr/bin/python
import constants

class Armor(Item):
    """
    Armor class.
    """

    def __init__(self, defense):
        Item.__init__(self, name, description, weight)
        self.defense = defense

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.ARMOR
