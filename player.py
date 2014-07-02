#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
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
        self._money     = constants.PlayerInitialization.MONEY

        #Initialize player stats
        self._experience = constants.PlayerInitialization.EXPERIENCE
        self._level = constants.PlayerInitialization.LEVEL
        
        self._hp = self._level * constants.HP_STAT
        self._maxHp = self._level * constants.HP_STAT
        self._totalMaxHp = self._level * constants.HP_STAT
        self._attack = self._level * constants.ATTACK_STAT
        
        #Initialize player inventory and equipment
        self._inventory = ItemSet()
        self._equipped = ItemSet()

        #Initialize items bonuses
        self._weaponAttack = constants.PlayerInitialization.WEAPON_ATTACK
        self._armorDefense = constants.PlayerInitialization.ARMOR_DEFENSE
        
        self._charmAttack = constants.PlayerInitialization.CHARM_ATTACK
        self._charmDefense = constants.PlayerInitialization.CHARM_DEFENSE
        self._charmHp = constants.PlayerInitialization.CHARM_HP

        self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
        self._totalDefense = self._armorDefense + self._charmDefense
        self._totalMaxHp = self._maxHp + self._charmHp
        
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
        target.takeAttack(self._totalAttack)
        
    def getAttack(self):
        """
        Gets a player's total attack power (excluding items).
        
        @return:          Base player attack.
        """
        return self._attack

    def getTotalAttack(self):
        """
        Gets player's total attack power (including items).

        @return:          Total player attack value.
        """
        return self._totalAttack

    def takeAttack(self, attack):
        """
        Allows player to receive an attack.

        @param attack:     The attack player is to receive.
        """
        self._hp = max(self._hp - max(attack - self._totalDefense, 0), 0)
        
    def getTotalDefense(self):
        """
        Returns player's total defense.
        
        @return:     Player's total defense stat.
        """
        return self._totalDefense
        
    def getCharmAttack(self):
        """
        Returns player's charm attack.
        
        @return:     Player's charm attack stat.
        """
        return self._charmAttack
        
    def getCharmDefense(self):
        """
        Returns player's charm defense.
        
        @return:     Player's charm stat.
        """
        return self._charmDefense
        
    def getCharmHp(self):
        """
        Returns player's charm hp.
        
        @return:     Player's charm hp stat.
        """
        return self._charmHp
        
    def getExperience(self):
        """
        Return's player experience.
        
        @return:    Returns player experience.
        """
        return self._experience

    def increaseExperience(self, newExperience):
        """
        Allows player to receive additional experience.
        Runs _updateLevel() upon receiving additional
        experience.

        @param newExperience:    The experience player is to receive.
        """
        self._experience += newExperience
        self._updateLevel()
        
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
        #Checks to see if player is max level
        if self._level == constants.MAX_LEVEL:
            return
        #Checks to see if player has leveled up
        if self._level != floor(self._experience/20) + 1:
            self._level = floor(self._experience/20) + 1
            self._level = int(self._level)

            #Player has leveled up. Updates player level and stats.
            print "\n%s leveled up! %s is now level %s!" \
                  % (self._name, self._name, self._level)
            self._maxHp = self._level * constants.HP_STAT
            self._totalMaxHp = self._maxHp + self._charmHp
            self._attack = self._level * constants.ATTACK_STAT
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
                  
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
        
    def getTotalMaxHp(self):
        """
        Returns player maximum hp, including charms.

        @return:    Player maximum hp.
        """
        return self._totalMaxHp
        
    def heal(self, amount):
        """
        Allows player to heal up to maximum starting hp.

        @param amount:    The amount of hp to be healed.
        """
        #If amount that player may be healed is less than amount possible
        if self._totalMaxHp - self._hp < amount:
            amountHealed = self._totalMaxHp - self._hp
        #If amount that player may be healed is equal to or more than amount possible
        else:
            amountHealed = amount
            
        self._hp += amountHealed

    def equip(self, item):
        """
        Allows a character to equip an item.
        
        Preconditions:
        -Item in inventory.
        -Item is instance of Armor or Weapon.
        -Item is not currently in self._equipped.

        @param item:    The item to be equipped.
        """
        #Check to see that preconditions are met
        if item not in self._inventory:
            print "%s not currently in inventory." % item.getName()
            return
        if not (isinstance(item, Armor) or isinstance(item, Weapon) or isinstance(item, Charm)):
            print "Item must be a weapon, armor, or charm."
            return
        if item in self._equipped:
            print "%s already equipped." % item.getName()
            return
        
        #Unequip currently equipped armor/weapon if necessary
        for currentItem in self._equipped:
            if isinstance(item, Weapon) and isinstance(currentItem, Weapon):  
                self.unequip(currentItem)
            elif isinstance(item, Armor) and isinstance(currentItem, Armor):
                self.unequip(currentItem)

        #Equip new item
        if isinstance(item, Weapon):
            self._equipped.addItem(item)
            self._weaponAttack = item.getAttack()
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
        elif isinstance(item, Armor):
            self._equipped.addItem(item)
            self._armorDefense = item.getDefense()
            self._totalDefense = self._armorDefense + self._charmDefense
        elif isinstance(item, Charm):
            self._equipped.addItem(item)
            self._charmAttack += item.getAttack()
            self._charmDefense += item.getDefense()
            self._charmHp += item.getHp()
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
            self._totalDefense = self._armorDefense + self._charmDefense
            self._totalMaxHp = self._maxHp + self._charmHp
        
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
                self._weaponAttack = 0
                self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
            if isinstance(item, Armor):
                self._armorDefense = 0
                self._totalDefense = self._armorDefense + self._charmDefense
            if isinstance(item, Charm):
                charmAttack = item.getAttack()
                charmDefense = item.getDefense()
                charmHp = item.getHp()
                
                self._charmAttack -= charmAttack
                self._charmDefense -= charmDefense
                self._charmHp -= charmHp
                
                self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
                self._totalDefense = self._armorDefense + self._charmDefense
                self._totalMaxHp = self._maxHp + self._charmHp
                
            print "%s unequipped %s." % (self._name, item.getName())
            
        else:
            print "%s not in equipped items." % item.getName()

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
        if amount < 0:
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

        @return:    True if possible, False otherwise.
        """
        exit = self._location.getExit(constants.Direction.NORTH)

        if exit:
            return True
        return False

    def canMoveSouth(self):
        """
        Determines if player can move south.

        @return:    True if possible, False otherwise.
        """
        exit = self._location.getExit(constants.Direction.SOUTH)

        if exit:
            return True
        return False

    def canMoveEast(self):
        """
        Determines if player can move east.

        @return:    True if possible, False otherwise.
        """
        exit = self._location.getExit(constants.Direction.EAST)

        if exit:
            return True
        return False

    def canMoveWest(self):
        """
        Determines if player can move west.

        @return:    True if possible, False otherwise.
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