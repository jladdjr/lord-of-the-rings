#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from items.weapon import Weapon
from items.armor import Armor
from stats import Stats
from math import floor

#TODO: Get startingInventory from GameLoader instead
from items.starting_inventory import startingInventory
###Need this too###
from items.starting_inventory import startingEquipment

import constants

class Player(object):
    """
    A character in your party. For instance, "Frodo."
    """
    
    def __init__(self, name, location):
        """
        Initializes the player.
        
        @param name:             The name of the player (e.g. "Frodo").
        @param location:         The location of player.
        """
        self._name      = name
        self._location  = location
        self._inventory = ItemSet(startingInventory)

        #Equip player with startingInventory
        self._equipped = []
        for item in startingEquipment:
            self.equip(item)

        #Initialize player stats
        self._experience = constants.STARTING_EXPERIENCE
        self._level = None
        self._levelUp

    def getInventory(self):
        """
        Returns the player's inventory.

        @return:    Player's inventory.
        """
        return self._inventory

    def attack(self, target):
        """
        Allows player to attack target. 

        @param target:     The target player is to attack.
        """
        self._totalDamage = self._attack + self._weaponAttack
        target.takeDamage(self._totalDamage)

    def takeDamage(self, damage):
        """
        Allows player to receive damage.

        @param damage:     The damage player is to receive.
        """
        self._hp = self._hp - max(damage - self._armorDefense, 0)

    def increaseExperience(self, new_experience):
        """
        Allows player to receive additional experience.

        @param new_experience:    The experience player is to receive.
        """
        self._experience += new_experience
        
    def _levelUp(self):
        """
        Levels up player and updates player stats. 
        """
        #Checks to see if player has leveled up
        if self._level != floor(self._experience/20) + 1:
            self._level = floor(self._experience/20) + 1

            #Player has leveled up. Updates player level and stats.
            print "%s leveled up! %s is now level %s" \
                  %(self._name, self._name, self._level)
            self._stats = Stats(self._level)
            self._newStats = stats.getStats()
            self._hp = self._stats[0]
            self._damage = self._stats[1]
            print "%s now has %s damage and %s hp!" \
                  %(self._name, self._damage, self._hp)

    def equip(self, item):
        """
        Allows a character to equip an item in inventory.

        @param item:    The item to be equipped.
        """
        if not (isinstance(item, Item) and (item in self._inventory) \
                and (isinstance(item, Armor) or isinstance(item, Weapon)):
            print "Cannot equip %s" %(self._item)
            
        else:
            if item in self._equipped:
                print "%s already equipped!" %(item)

            else:
                self._equipped.append(item)
                #Update player to reflect equipment
                if isinstance(item, Armor):
                    self._armor = item
                    self._armorDefense = self._armor.getDefense()
                if isinstance(item, Weapon):
                    self._weapon = item
                    self._weaponAttack = self._weapon.getDamage()
                    
                print "%s equipped %s." %(self._name, self._item)
            
    def unequip(self, item):
        """
        Allows a character to unequip a currently equipped item.

        @param item:    The item to be unequipped.
        """
        if isinstance(item, Item) and (item in self._inventory) \
           and (isinstance(item, Armor) or isisntance(item, Weapon)):
            self._equipped.remove(item)
            
            #Update player to reflect equipment
            if isinstance(item, Armor):
                self._armor = None
                self._armorDefense = 0
            if isinstance(item, Weapon):
                self._weapon = None
                self._weaponAttack = 0
                
            print "%s unequipped %s." %(self._name, self._item)
        else:
            print "Cannot unequip %s." %(self._item)

    def getInventory(self):
        """
        Returns the player's inventory.

        @return:    Player's inventory.
        """
        return self._inventory

    def getEquipped(self):
        """
        Returns the player's currently equipped equipment.

        @return:    Player's current gear.
        """
        return self._equipped

    def moveNorth(self):
        pass
        #TODO: Consider replacing this with moveNorth(), moveSouth(), etc.
        #      methods. (Or, create a move() method that takes a direction
        #      (which should be defined in constants). -JDL

    def moveSouth(self):
        pass

    def moveEast(self):
        pass

    def moveWest(self):
        pass

    def getLocation(self):
        """
        Returns player's current location (i.e. space).

        @return:    Player's current location.
        """
        return self._location
