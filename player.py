#!/usr/bin/python

from items import Items

class Player(object):
    """
    Represents the (human) player.
    """
    def __init__(self, location):
        """
        Initializes the player. Player is a party that contains different members.
        """
        
        self._location = location
        self._inventory = Items()
        for item in None:
            self._inventory.addItem(item)

    def getLocation(self):
        return self._location
