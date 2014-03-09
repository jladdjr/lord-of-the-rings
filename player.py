#!/usr/bin/python

#TODO: Create methods related to Hp, attack, etc.

from items.item import Item
from items.item_set import ItemSet
from items.weapon import Weapon
from items.armor import Armor
from stats import Stats
from math import floor

#TODO: Get startingInventory from GameLoader instead
from items.starting_inventory import startingInventory
#from items.starting_inventory import startingEquipment

import constants

class Player(object):
    """
    Represents the (human) player.
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
        self._equipped = ItemSet()
        
        #TODO: Chris add startingEquipment
        #for item in startingEquipment:
        #    self.equip(item)

        #Initialize player stats
        self._experience = constants.STARTING_EXPERIENCE
        self._level = 0
        self._updateLevel()
        self._weaponAttack = 0
        self._armorDefense = 0

    def attack(self, target):
        """
        Allows player to attack target. 

        @param target:     The target player is to attack.
        """
        self._totalAttack = self._attack + self._weaponAttack
        target.takeAttack(self._totalAttack)
        
    def getAttack(self):
        """
        Gets a player's total attack power (including items).
        
        @return:    player attack + weapon attack
        """
        return self._attack + self._weaponAttack

    def takeAttack(self, attack):
        """
        Allows player to receive an attack.

        @param attack:     The attack player is to receive.
        """
        self._hp = self._hp - max(attack - self._armorDefense, 0)
        
    def getExperience(self):
        """
        Return's player experience.
        
        @return:    return's player experience.
        """
        return self._experience

    def increaseExperience(self, newExperience):
        """
        Allows player to receive additional experience.

        @param newExperience:    The experience player is to receive.
        """
        self._experience += new_experience
        
    def getLevel(self):
        """
        Return's player level.
        
        @return:   return's player level.
        """
        return self._level
        
    def _updateLevel(self):
        """
        Levels up player and updates player stats. 
        """
        #Checks to see if player has leveled up
        if self._level != floor(self._experience/20) + 1:
            self._level = floor(self._experience/20) + 1

            #Player has leveled up. Updates player level and stats.
            print "%s leveled up! %s is now level %s" \
                  %(self._name, self._name, self._level)
            self._hp = self._level * constants.HP_STAT
            self._attack = self._level * constants.ATTACK_STAT
                  
    def getHp(self):
        """
        Returns player Hp.

        @return: player Hp.
        """
        return self._hp
        
    def getAttack(self):
        """
        Returns player attack.
        
        @return: player attack.
        """
        return self._attack

    def equip(self, item):
        """
        Allows a character to equip an item in inventory.

        @param item:    The item to be equipped.
        """
        if not (item in self._inventory) \
            or not (isinstance(item, Armor) or isinstance(item, Weapon)) \
            or item in self._equipped:
            print "Cannot equip %s" %item

        else:
            self._equipped.addItem(item)
            #Update player to reflect equipment
            if isinstance(item, Armor):
                self._armor = item
                self._armorDefense = self._armor.getDefense()
            if isinstance(item, Weapon):
                self._weapon = item
                self._weaponAttack = self._weapon.getAttack()
                    
            print "%s equipped %s." %(self._name, item)
            
    def unequip(self, item):
        """
        Allows a character to unequip a currently equipped item.

        @param item:    The item to be unequipped.
        """
        if item in self._equipped:
            self._equipped.removeItem(item)
            
            #Update player to reflect equipment
            if isinstance(item, Armor):
                self._armor = None
                self._armorDefense = 0
            if isinstance(item, Weapon):
                self._weapon = None
                self._weaponAttack = 0
                
            print "%s unequipped %s." %(self._name, item)
            
        else:
            print "Cannot unequip %s." %(item)

    def getEquipped(self):
        """
        Returns the player's currently equipped equipment.

        @return:    Player's current gear.
        """
        return self._equipped._items
    
    def addInventory(self, item):
        """
        Adds an item to inventory.
        """
        if isinstance(item, Item) and (item not in self._inventory):
            print "Added %s to inventory."
            self._inventory.addItem(item)
        else:
            print "Cannot add %s to inventory." %(item)
    
    def getInventory(self):
        """
        Returns the player's inventory.

        @return:    Player's inventory.
        """
        return self._inventory

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
