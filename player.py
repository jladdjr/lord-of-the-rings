#!/usr/bin/python

from items import Items
import constants

class Player(object):
    """
    Represents the (human) player.
    """
    def __init__(self):
        """
        Initializes the player. Player is a party that contains different members.
        """
        self._inventory = Items(self, constants.base_set) 

    
