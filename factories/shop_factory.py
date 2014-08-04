#!/usr/bin/python

import math
import random

from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item_set import ItemSet
from items.unique_items import lowLevelFindableUniques, shopWeaponDist, shopArmorDist, shopPotionDist
import constants

def getItems(region, numItems, quality):
    """
    Generates random items for shop.

    @param region:       The region the shop is in.
    @param numItems:     The number of items to generate
    @param quality:      Integer from 0-20 that determines quality of items 
                         generated.
    @return:             A list of randomly generated item objects.
    """
    items = ItemSet()

    for item in range(numItems):
        #Generate random number used in determining item type
        randType = random.random()
        
        #Randomize quality
        quality = qualityRandomizer(quality)
        
        #Generate items and append to items list
        if randType < constants.ShopFactoryConstants.WEAPON_UPPER_LIMIT:
            item = genWeapon(quality, region)
            items.addItem(item)
        elif randType < constants.ShopFactoryConstants.ARMOR_UPPER_LIMIT:
            item = genArmor(quality, region)
            items.addItem(item)
        elif randType < constants.ShopFactoryConstants.POTION_UPPER_LIMIT:
            item = genPotion(quality, region)
            items.addItem(item)
        else:
            #Only shops advanced in the game generate uniques
            if (constants.ShopFactoryConstants.UNIQUE_QUALITY_REQ <= 
                quality and lowLevelFindableUniques):
                item = random.choice(lowLevelFindableUniques)
                items.addItem(item)
            #Low-level shops generate additional potions
            else:
                item = genPotion(quality, region)
                items.addItem(item)
                
    return items
    
def qualityRandomizer(quality):
    """
    Randomizes quality with a normal distribution.
    
    @param quality:    Shop item quality.
    
    @return:           Randomized quality.
    """
    #Normalize quality with normal distribution
    quality = random.normalvariate(quality, 
        constants.ShopFactoryConstants.STANDARD_DEVIATION)
    quality = math.floor(quality)
    
    #Make sure that results are within bounds
    if quality < constants.ShopFactoryConstants.QUALITY_MINIMUM:
        quality = constants.ShopFactoryConstants.QUALITY_MINIMUM
    if quality > constants.ShopFactoryConstants.QUALITY_MAXIMUM:
        quality = constants.ShopFactoryConstants.QUALITY_MAXIMUM
    
    return quality
    
def genWeapon(quality, region):
    """
    Generates a weapon.
    
    @param quality:     Quality of item.
    @param region:      Shop region.
    
    @return:            Spawned weapon.
    """
    regionalDist = shopWeaponDist[region]
    acceptableItems = []
    
    #Create bounds
    for weapon in regionalDist:
        lowerBound = regionalDist[weapon][0]
        higherBound = regionalDist[weapon][1]
        
        #Find items within bounds
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(weapon)
    
    #Select randomly drawn item from acceptableItems
    item = random.choice(acceptableItems)
    return item
    
def genArmor(quality, region):
    """
    Generates a piece of armor.
    
    @param quality:     Quality of item.
    @param region:      Shop region.
    
    @return:            Spawned weapon.
    """
    regionalDist = shopArmorDist[region]
    acceptableItems = []
    
    #Create bounds
    for armor in regionalDist:
        lowerBound = regionalDist[armor][0]
        higherBound = regionalDist[armor][1]
        
        #Find items within bounds
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(armor)
    
    #Select randomly drawn item from acceptableItems
    item = random.choice(acceptableItems)
    return item
    
def genPotion(quality, region):
    """
    Generates a potion.
    
    @param quality:     Quality of item.
    @param region:      Shop region.
    
    @return:            Spawned weapon.
    """
    regionalDist = shopPotionDist[region]
    acceptableItems = []
    
    #Create bounds
    for potion in regionalDist:
        lowerBound = regionalDist[potion][0]
        higherBound = regionalDist[potion][1]
        
        #Find items within bounds
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(potion)
    
    #Select randomly drawn item from acceptableItems
    item = random.choice(acceptableItems)
    return item