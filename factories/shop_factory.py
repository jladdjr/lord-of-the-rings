#!/usr/bin/python

import math
from items.potions import Potions
from items.armor import Armor

def getItems(self, numItems, quality):
    """
    generates items for the shop.
    As of 03.26.2014 half (rounded down) are potions and the rest are branches
    """
    
    numPotions = numItems*0.5
    numPotions = math.floor(numPotions)
    numArmor = numItems - numPotions
    
    items = []
    
    #make generic potions
    for i in numPotions:
        newPotion = Potion("generic potion", "no description", 1, 1)
        items.append(newPotion)
    for i in numArmor:
        newArmor = Armor("branch", "a bit bigger than a twig", 0, 0)
        items.append(newArmor)
    
    print "contains: ", items
    return items
