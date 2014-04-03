#!/usr/bin/python

import random
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion

def getItems(numItems, quality):
    """
    Generates random items for shop.

    @param numItems:     The number of items to generate
    @param quality:      Integer from 1-20 that determines quality of items generated.
    """
    items = []
    for item in range(numItems):
        #Generate random numbers to determine item spawn type
        seed = random.random()
        seedDescription = random.random()
        
        #Create weapon
        if seed < .3:
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
            if quality <5:
                suffix = "of Traveling"
            elif 5 <= quality < 10:
                suffix = "of Defending"
            elif 10 <= quality < 15:
                suffix = "of Hacking"
            else:
                suffix = "of Ruling"
            #Generate weapon type
            if seed < .25:
                type = "Sword"
                weight = 2
                damage = 2
            elif .25 <= seed < .5:
                type = "Staff"
                weight = 3
                damage = 4
            elif .5 <= seed < .75:
                type = "Scepter"
                weight = 2
                damage = 6
            else:
                type = "Axe"
                weight = 4
                damage = 8

            #Concatenate name
            totalName = prefix + " " + type + " " + suffix

            #Generate description
            if seedDescription < .5:
                description = "Once owned by a Thorin Oakenshield"
            else:
                description = "Unknown origin"

            #Generate cost
            cost = 1 * quality
            
            #Generate weapon
            weapon = Weapon(totalName, description, weight, damage, cost)
            items.append(weapon)
            
        #Create armor
        elif .3 <= seed < .6:
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
                prefix = "of Ruling"
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
                defense = 4
                
            #Concatentate name
            name = prefix + " " + type + " " + suffix

            #Generate description
            if seedDescription < .5:
                description = "Gondorian in origin"
            else:
                description = "Made in Rohan"

            #Generate cost
            cost = 2 * quality
            
            #Generate armor
            armor = Armor(name, description, weight, defense, cost)
            items.append(armor)
            
        #Create potion
        else:
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
            if seedDescription < .5:
                description = "A light tonic"
            else:
                description = "A strange concoction"

            #Generate weight
            weight = 1
            
            #Generate potion
            potion = Potion(name, description, weight, healing, cost)
            items.append(potion)
    return items
