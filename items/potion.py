#!/usr/bin/python

from items.item import Item
from constants import ItemType

class Potion(Item):
    """
    Potions are a child class of Item. 
    
    Potions are a one-time use item that serve to heal player. Potions 
    heal according to their defining parameter, healing. 
    """
    def __init__(self, name, description, weight, cost, healing):
        """
        Initializes potions class.

        @param name:          Name of portion.
        @param description:   Description of potion.
        @param weight:        Weight of weapon.
        @param cost:          The cost of the potion.
        @param healing:       Healing stat of potion. Player may heal at most 
                              this amount upon use.
        """
        Item.__init__(self, name, description, weight, cost)
        
        self._healing = healing
        
    def getHealing(self):
        """
        Returns potion healing value.

        @return: Potion healing value.
        """
        return self._healing

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.POTION
