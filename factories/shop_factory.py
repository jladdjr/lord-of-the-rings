#!/usr/bin/python

import random
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
import constants

def getItems(numItems, quality):
    """
    Generates random items for shop.

    @param numItems:     The number of items to generate
    @param quality:      Integer from 1-20 that determines quality of items generated.
    @return:             A list of randomly generated item objects.
    """
    items = []
    for item in range(numItems):
        #Generate random numbers for item generation
        randType = random.random()
        randWeaponType = random.random()
        randDesc = random.random()

        #Generate items and append to items list
        if randType < .3:
            item = genWeapon(quality, randWeaponType, randDesc)
            items.append(item)
        elif .3 <= randType < .6:
            item = genArmor(quality, randDesc)
            items.append(item)
        else:
            item = genPotion(quality, randDesc)
            items.append(item)

    return items

#Generate weapon
def genWeapon(quality, randWeaponType, randDesc):
    """
    Generates a single weapon object.

    @param quality:         The quality (1-20) of the weapon.
    @param randTypeWeapon:  Random number that determines the type of weapon generated.
    @param randDesc:        Random number that determines the description of the item.
    @return:                The randomly generated weapon.
    """
    #Generate prefix
    if quality < 5:
        prefix = "Light"
    elif 5 <= quality < 10:
        prefix = "Medium"
    elif 10 <= quality < 15:
        prefix = "Heavy"
    else:
        prefix = "Legendary"
    #Generate suffix
    if quality < 5:
        suffix = "of Travel"
    elif 5 <= quality < 10:
        suffix = "of Defense"
    elif 10 <= quality < 15:
        suffix = "of Hacking"
    else:
        suffix = "of Domination"
    #Generate weapon type
    if randWeaponType < .25:
        type = "Sword"
        weight = 2
        damage = 2
    elif .25 <= randWeaponType < .5:
        type = "Staff"
        weight = 3
        damage = 2
    elif .5 <= randWeaponType < .75:
        type = "Scepter"
        weight = 2
        damage = 3
    else:
        type = "Axe"
        weight = 4
        damage = 4

    #Concatenate name
    totalName = prefix + " " + type + " " + suffix

    #Generate weapon description
    description = genWeaponDescription(randDesc)

    #Generate cost
    cost = quality * constants.WEAPON_COST
            
    #Generate weapon
    weapon = Weapon(totalName, description, weight, damage, cost)
    return weapon

#Generate weapon description
def genWeaponDescription(randDesc):
    """
    Generates random weapon description.

    @param randDesc:   Random number used to generate item description.
    @return:           The description of the weapon.
    """
    if randDesc < .1:
        description = "Once owned by a Thorin Oakenshield"
    elif .1 <= randDesc < .2:
        description = "Extremely shiny"
    elif .2 <= randDesc < .3:
        description = "Makes strange sounds"
    elif .3 <= randDesc < .4:
        description = "Seems to have magical properties"
    elif .4 <= randDesc < .5:
        description = "Supposedly lucky"
    elif .5 <= randDesc < .6:
        description = "Very sharp"
    elif .6 <= randDesc < .7:
        description = "Doesn't feel right"
    elif .7 <= randDesc < .8:
        description = "Larger than what you'd expect"
    elif .8 <= randDesc < .9:
        description = "From Rohan"
    else:
        description = "Unknown origin"
        
    return description

#Generate armor
def genArmor(quality, randDesc):
    """
    Generates random piece of armor.

    @param quality:      The quality statistic (1-20) used to determine armor statistics.
    @param randDesc:     Random number used to generate armor description.
    @return:             A randomly generated armor object.
    """
    #Generate prefix
    if quality < 5:
        prefix = "Light"
    elif 5 <= quality < 10:
        prefix = "Rugged"
    elif 10 <= quality < 15:
        prefix = "Heavy"
    else:
        prefix = "Legendary"
    #Generate suffix
    if quality < 5:
        suffix = "of Training"
    elif 5 <= quality < 10:
        suffix = "of Travel"
    elif 10 <= quality < 15:
        suffix = "of Battle"
    else:
        prefix = "of Honor"
    #Generate armor type
    if quality < 5:
        type = "Leather Cloak"
        weight = 4
        defense = 1
    elif 5 <= quality < 10:
        type = "Chainmail"
        weight = 7
        defense = 2
    elif 10 <= quality < 15:
        type = "Platemail"
        weight = 10
        defense = 3
    else:
        type = "Mithril Shroud"
        weight = 0
        defense = 5
                
    #Concatentate name
    name = prefix + " " + type + " " + suffix

    #Generate description
    description = genArmorDescription(randDesc)

    #Generate cost
    cost = quality * constants.ARMOR_COST
            
    #Generate armor
    armor = Armor(name, description, weight, defense, cost)

    return armor

#Generate armor description
def genArmorDescription(randDesc):
    """
    Generates armor description.

    @param randDesc:   Generates armor description.
    @return:           Armor description.
    """
    if randDesc < .1:
        description = "Very thick"
    elif .1 <= randDesc < .2:
        description = "Covered in blood"
    elif .2 <= randDesc < .3:
        description = "Seems strange"
    elif .3 <= randDesc < .4:
        description = "Very sturdy"
    elif .4 <= randDesc < .5:
        description = "Extremely old"
    elif .5 <= randDesc < .6:
        description = "Has strange runes and symbols"
    elif .6 <= randDesc < .7:
        description = "From the ancient Numernorians"
    elif .7 <= randDesc < .8:
        description = "Completely pitch black"
    elif .8 <= randDesc < .9:
        description = "Many colors"
    else:
        description = "Strange design"
        
    return description

#Generate potion:
def genPotion(quality, randDesc):
    """
    Generates potion object.

    @param quality:   Quality statistic (1-20) that determines potion attributes.
    @param randDesc:  Random number used to generate potion description.
    @return:          A potion object. 
    """
    #Generate prefix
    if quality < 5:
        prefix = "Light"
        healing = 2
        cost = 1
    elif 5 <= quality < 10:
        prefix = "Medium"
        healing = 5
        cost = 2
    elif 10 <= quality < 15:
        prefix = "Heavy"
        healing = 10
        cost = 4
    else:
        prefix = "Legendary"
        healing = 20
        cost = 8

    #Concatenate name
    name = prefix + " Potion of Healing"

    #Generate description
    description = genPotionDescription(randDesc)
    
    #Generate weight
    weight = 1
            
    #Generate potion
    potion = Potion(name, description, weight, healing, cost)
    
    return potion

#Generate potion description
def genPotionDescription(randDesc):
    """
    Generates potion description.

    @param randDesc:   The random number used to generate potion description.
    @return:           The description of the potion. 
    """
    if randDesc < .25:
        description = "Smells strange"
    elif .25 <= randDesc < .5:
        description = "Looks disgusting"
    elif .5 <= randDesc < .75:
        description = "Crystal clear"
    else:
        description = "Slightly intoxicating"
        
    return description
