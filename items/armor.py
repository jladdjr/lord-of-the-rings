#!/usr/bin/python

from items.item import Item
from constants import ItemType

class Armor(Item):
    """
    Armor is a child class of Item.
    
    Armor serves as the class of defensive items in the game. It has a 
    special attribute, "defense," which serves to reduce the damage that 
    player receives.
    """
    def __init__(self, name, description, weight, cost, defense):
        """
        Initializes armor class.

        @param name:         The name of the piece of armor.
        @param description:  Armor description.
        @param weight:       Armor weight.
        @param cost:         The cost of the armor.
        @param defense:      The defense stat of the piece of armor. 
        """
        Item.__init__(self, name, description, weight, cost)
        
        self._defense = defense
        
    def getDefense(self):
        """
        Returns the armor's defense stat.

        @return:    Armor defense.
        """
        return self._defense

    def getType(self):
        """
        Returns the item's type.

        @return:   Item's type.
        """
        return ItemType.ARMOR