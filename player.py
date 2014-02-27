#!/usr/bin/python

from items import Items
from startinginventory import startingInventory
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
        self._name = name
        self._location = location
        self._inventory = Items(startingInventory)

        self._level = constants.startingLevel
        self._experience = constants.startingExperience

        self._attack = self._level * constants.attackStat
        self._hp = self._level * constants.hpStat

    def attack(self, target):
        """
        Allows player to attack target.

        @param target:     The target player is to attack.
        """
        target.takeDamage(self._attack)
        print "%s attacked %s for %s damage!" %(self._name, target, self._attack)

    def takeDamage(self, damage):
        """
        Allows player to receive damage.

        @param damage):    The damage player is to receive.
        """
        self._hp -= damage
        print "%s took %s damage!" %(self._name, self._attack)

    def levelUp(self):
        """
        Levels up player and updates player stats. 
        """
        pass

    def updateLocation(self, newLocation):
        self._location = newLocation

    def getLocation(self):
        return self._location

    
        
