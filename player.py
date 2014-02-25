#!/usr/bin/python

from items import Items
from startinginventory import startingInventory

class Player(object):
    """
    Represents the (human) player.
    """
    
    def __init__(self, location):
        """
        Initializes the player. Player is a party that contains different members.

        @param location:         The location of player.
        """
        self._location = location
        self._inventory = Items(startingInventory)

    def updateLocation(self, newLocation):
        self._location = newLocation

    def getLocation(self):
        return self._location

    
