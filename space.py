#!/usr/bin/python

from items.item_set import ItemSet

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """
    
    def __init__(self, name):
        """
        Intialize a Space object.
        """
        self._items = ItemSet()
        self._name = name

    def getName(self):
        """
        Returns the name of the room.
        """
        return self._name

    def addItem(self, item):
        """
        Adds an item to the room.

        @param item:    Item to add.
        """
        self._items.addItem(item)

    def removeItem(self, item):
        """
        Removes an item from the room.

        @param item:    Item to remove.
        """
        self._items.removeItem(item)

    def containsItem(self, item):
        """
        Determines if room contains an item.

        @param item:    Item to search for.
        """
        #TODO:  Currently this method takes
        #       an actual object as a parameter.
        #
        #       Need to create method that
        #       searches for an object by name
        #       instead.  -JDL

        return self._items.containsItem(item)

    def getItemSet(self):
        """
        Returns items contained by room.
        (i.e. An ItemSet object).
        
        @return: An ItemSet object containing 
        set of items found in room.
        """
        return self._items
