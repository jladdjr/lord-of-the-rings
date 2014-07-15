#!/usr/bin/python

import random

from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.unique_items import lowLevelFindableUniques
import constants

def getItems(region, numItems, quality):
    """
    Generates random items for shop.

    @param region:       The region the shop is in.
    @param numItems:     The number of items to generate
    @param quality:      Integer from 1-20 that determines quality of items 
                         generated.
    @return:             A list of randomly generated item objects.
    """
    items = []
    for item in range(numItems):
        #Generate random numbers for item generation
        randType = random.random()
        randWeaponType = random.random()
        randDesc = random.random()

        #Generate items and append to items list
        if randType < constants.ShopFactoryConstants.WEAPON_UPPER:
            item = genWeapon(quality, randWeaponType, randDesc)
            items.append(item)
        elif constants.ShopFactoryConstants.ARMOR_LOWER <= randType < constants.ShopFactoryConstants.ARMOR_UPPER:
            item = genArmor(quality, randDesc)
            items.append(item)
        elif constants.ShopFactoryConstants.POTION_LOWER <= randType < constants.ShopFactoryConstants.POTION_UPPER:
            item = genPotion(quality, randDesc)
            items.append(item)
        else:
            #Only shops advanced in the game generate uniques
            if 10 <= quality and lowLevelFindableUniques:
                item = random.choice(lowLevelFindableUniques)
                lowLevelFindableUniques.remove(item)
                items.append(item)
            #Low-level shops generate additional potions
            else:
                item = genPotion(quality, randDesc)
                items.append(item)
                
    return items