#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from math import floor

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
        self._money     = constants.STARTING_MONEY

        #Initialize player inventory and equipment
        self._inventory = ItemSet()
        self._equipped = ItemSet()

        #Initialize player stats
        self._experience = constants.STARTING_EXPERIENCE
        self._level = constants.STARTING_LEVEL
        
        self._hp = self._level * constants.HP_STAT
        self._maxHp = self._level * constants.HP_STAT
        self._attack = self._level * constants.ATTACK_STAT

        #Initialize items bonuses
        self._weaponAttack = 0
        self._totalAttack = self._attack + self._weaponAttack
        self._armorDefense = 0

    def getName(self):
        """
        Returns player name.

        @return:          The name of the player.
        """
        return self._name

    def attack(self, target):
        """
        Allows player to attack target. 

        @param target:    The target player is to attack.
        """
        self._totalAttack = self._attack + self._weaponAttack
        target.takeAttack(self._totalAttack)
        
    def getAttack(self):
        """
        Gets a player's total attack power (including items).
        
        @return:          Sum of player attack and weapon attack.
        """
        return self._totalAtack

    def takeAttack(self, attack):
        """
        Allows player to receive an attack.

        @param attack:     The attack player is to receive.
        """
        self._hp = max(self._hp - max(attack - self._armorDefense, 0), 0)
        
    def getExperience(self):
        """
        Return's player experience.
        
        @return:    Returns player experience.
        """
        return self._experience

    def increaseExperience(self, newExperience):
        """
        Allows player to receive additional experience.

        @param newExperience:    The experience player is to receive.
        """
        self._experience += newExperience
        
    def getLevel(self):
        """
        Return's player level.
        
        @return:      Player level.
        """
        return self._level
        
    def _updateLevel(self):
        """
        Levels up player and updates player stats. 
        """
        #Checks to see if player has leveled up
        if self._level == constants.MAX_LEVEL:
            return
        if self._level != floor(self._experience/20) + 1:
            self._level = floor(self._experience/20) + 1

            #Player has leveled up. Updates player level and stats.
            print "%s leveled up! %s is now level %s" \
                  % (self._name, self._name, self._level)
            self._maxHp = self._level * constants.HP_STAT
            self._attack = self._level * constants.ATTACK_STAT
            self._totalAttack = self._attack + self._weaponAttack
                  
    def getHp(self):
        """
        Returns player hp.

        @return:    Player hp.
        """
        return self._hp

    def getMaxHp(self):
        """
        Returns player maximum hp.

        @return:    Player maximum hp.
        """
        return self._maxHp
        
    def heal(self, amount):
        """
        Allows player to heal up to maximum starting hp.

        @param amount:    The amount of hp to be healed.
        """
        #If amount that player may be healed is less than amount possible
        if self._maxHp - self._hp < amount:
            amountHealed = self._maxHp - self._hp
        #If amount that player may be healed is equal to or more than amount possible
        else:
            amountHealed = amount
            
        self._hp += amountHealed

        print "%s got healed by %s! %s's health is now at %s" % (self._name, amountHealed, self._name, self._hp)

    def equip(self, item):
        """
        Allows a character to equip an item in inventory.
        
        Note: An item *must* be in the player's inventory
        before it can be equipped. The item must also
        be a piece of Armor or a Weapon.

        @param item:    The item to be equipped.
        """

		#TODO: Need to revisit the logic of this method.
		#      The method should take advantage of the unequip() method
        #      now that it exists.
        #
        #      After that change, review the overall logic
        #      to make sure it makes sense.

        #Check to see if item may be equipped
        if not (item in self._inventory) \
            or not (isinstance(item, Armor) or isinstance(item, Weapon)) \
            or item in self._equipped:
            print ""
            print "Cannot equip %s." %item.getName()
            return

        #Unequip currently equipped armor/weapon if necessary
        if isinstance(item, Armor):
            self._armor = item
            self._armorDefense = self._armor.getDefense()
        elif isinstance(item, Weapon):
            self._weapon = item
            self._weaponAttack = self._weapon.getAttack()

        for currentItem in self._equipped:
            if isinstance(item, Weapon) and isinstance(currentItem, Weapon):  
                self.unequip(currentItem)
            elif isinstance(item, Armor) and isinstance(currentItem, Armor):
                self.unequip(currentItem)
            
        #Update player to reflect equipment
        if isinstance(item, Armor):
            self._armor = item
            self._armorDefense = self._armor.getDefense()
        elif isinstance(item, Weapon):
            self._weapon = item
            self._weaponAttack = self._weapon.getAttack()

        self._equipped.addItem(item)
        
        print "%s equipped %s." %(self._name, item.getName())
            
    def unequip(self, item):
        """
        Allows a character to unequip a currently equipped item.

        @param item:    The item to be unequipped.
        """
        print ""
        if item in self._equipped:
            self._equipped.removeItem(item)
            
            #Update player to reflect equipment
            if isinstance(item, Weapon):
                self._weapon = None
                self._weaponAttack = 0
            if isinstance(item, Armor):
                self._armor = None
                self._armorDefense = 0
                
            print "%s unequipped %s." % (self._name, item.getName())
            
        else:
            print "Cannot unequip %s." % item.getName()

    def getWeapon(self):
        """
        Returns play weapon.

        @return:    Player's current weapon.
        """
        return self._weapon

    def getArmor(self):
        """
        Returns player armor.

        @return:    Player's current armor.
        """
        return self._armor

    def getEquipped(self):
        """
        Returns the player's currently equipped equipment.

        @return:    Player's current gear.
        """
        return self._equipped
    
    def addToInventory(self, item):
        """
        Adds an item to inventory.

        @param item:   The item to be added to inventory.
        """
        if (isinstance(item, Item) and (item not in self._inventory)):
            print "Added %s to inventory." % item.getName()
            self._inventory.addItem(item)
        else:
            print "Cannot add %s to inventory." % item

    def removeFromInventory(self, item):
        """
        Removes an item from inventory. If item is currently equipped, unequips item.

        @param item:   The item to be removed.
        """
        if item in self._inventory:
            if item in self._equipped:
                self.unequip(item)
            self._inventory.removeItem(item)
    
    def getInventory(self):
        """
        Returns the player's inventory.

        @return:    Player's inventory.
        """
        return self._inventory

    def getMoney(self):
        """
        Returns player's money.

        @return:    Player's money.
        """
        return self._money

    def increaseMoney(self, amount):
        """
        Increases player money.
        """
        if amount <= 0:
            errorMsg = "Method increaseMoney() was given a negative value"
            raise AssertionError(errorMsg)

        self._money += amount
        
    def decreaseMoney(self, amount):
        """
        Decreases player money.
        """
        if amount <= 0:
            errorMsg = "Method decreaseMoney() was given a negative value"
            raise AssertionError(errorMsg)

        self._money -= amount
    
    def canMoveNorth(self):
        """
        Determines if player can move north.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.NORTH)

        if exit:
            return True
        return False

    def canMoveSouth(self):
        """
        Determines if player can move south.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.SOUTH)

        if exit:
            return True
        return False

    def canMoveEast(self):
        """
        Determines if player can move east.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.EAST)

        if exit:
            return True
        return False

    def canMoveWest(self):
        """
        Determines if player can move west.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.WEST)

        if exit:
            return True
        return False


    def moveNorth(self):
        """
        Moves player north one space.
        """
        northSpace = self._location.getExit(constants.Direction.NORTH) 
        
        #If north space does not exist, do nothing
        if not northSpace:
            return
        #...otherwise, move to new space 
        self._location = northSpace

    def moveSouth(self):
        """
        Moves player south one space.
        """
        southSpace = self._location.getExit(constants.Direction.SOUTH)

        #If south space does not exist, do nothing
        if not southSpace:
            return
        #...otherwise, move to new space 
        self._location = southSpace 

    def moveEast(self):
        """
        Moves player east one space.
        """
        eastSpace = self._location.getExit(constants.Direction.EAST)

        #If east space does not exist, do nothing
        if not eastSpace:
            return
        #...otherwise, move to new space 
        self._location = eastSpace 

    def moveWest(self):
        """
        Moves player west one space.
        """
        westSpace = self._location.getExit(constants.Direction.WEST)

        #If west space does not exist, do nothing
        if not westSpace:
            return
        #...otherwise, move to new space 
        self._location = westSpace 

    def getLocation(self):
        """
        Returns player's current location (i.e. space).

        @return:    Player's current location.
        """
        return self._location
