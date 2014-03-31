#!/usr/bin/python

import math
from items.potion import Potion
from items.armor import Armor

def getItems(numItems, quality):
    """
    generates items for the shop.
    As of 03.26.2014 half (rounded down) are potions and the rest are branches
    """
    
    numPotions = numItems*0.5
    numPotions = int(math.floor(numPotions))
    numArmor = int(numItems - numPotions)
    
    items = []
    
    #make generic potions
    for i in range(numPotions):
        newPotion = Potion("generic potion", "no description", 1, 1)
        items.append(newPotion)
    for i in range(numArmor):
        newArmor = Armor("leaf", "a bit wider than a twig", 1, 0)
        items.append(newArmor)
    
    print "contains: ", items
    return items
