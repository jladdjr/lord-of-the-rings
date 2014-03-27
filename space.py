#!/usr/bin/python

from constants import Direction
from items.item_set import ItemSet

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """
    def __init__(self, name, description):
        """
        Initialize a Space object.
        """
        self._exits = { Direction.NORTH : None,
                        Direction.SOUTH : None,
                        Direction.EAST : None,
                        Direction.WEST : None }

        self._items = ItemSet()
        self._name = name
        self._description = description

    def getName(self):
        """
        Returns the name of the room.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of the room.
        """
        return self._description

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

        @param item:    Item object to search for.
        """
        return self._items.containsItem(item)

    def containsItemString(self, string):
        """
        Determines if room contains an item.

        @param item:     The string associated with the name of the item that we are looking for.
        """
        for item in self._items:
            if item.getName() == string:
                return True
            
        return False
    
    def getItemSet(self):
        """
        Returns items contained by room.
        (i.e. An ItemSet object).
        
        @return: An ItemSet object containing 
        set of items found in room.
        """
        return self._items

    def createExit(self, direction, space, outgoingOnly=False):
        """
        Create an exit to another space. By default,
        the method creates the appropriate exit
        in the second space. (This can be suppressed, however,
        using I{outgoingOnly}).

        @param direction:       Direction of exit.
        @param space:           Adjacent space.
        @keyword outgoingOnly:  By default, this method creates the appropriate
                                exit in the second space. Set I{outgoingOnly}
                                to False to supress this behavior.
        """
        #Make sure a valid direction has been specified
        if not self._isExit(direction):
            errorMsg = "Direction not valid: %s" % direction 
            raise AssertionError(errorMsg)

        #Set exit to other space
        self._exits[direction] = space

        #Create exit from other space to this space
        if not outgoingOnly:
            oppositeDirection = self._oppositeDirection(direction)
            space._exits[oppositeDirection] = self

    def clearExit(self, direction, outgoingOnly):
        """
        Removes an exit to another space. By default,
        the method removes the appropriate exit from
        the second space. (This can be suppressed, however,
        using I{outgoingOnly}).

        @param direction:       Direction of exit.
        @keyword outgoingOnly:  By default, this method removes the appropriate
                                exit from the second space. Set I{outgoingOnly}
                                to False to suppress this behavior.
        """
        #Make sure a valid direction has been specified
        if not self._isExit(direction):
            errorMsg = "Direction not valid: %s" % direction 
            raise AssertionError(errorMsg)

        #If exit has not been set, there is nothing to do
        if self._exits[direction] == None:
            return

        #Create a temporary copy of adjacent space
        adjSpace = self._exits[direction]

        #Clear exit from this space
        self._exits[direction] = None

        #Clear exit from other space to this space
        if not outgoingOnly:
            oppositeDirection = self._oppositeDirection(direction)
            adjSpace._exits[oppositeDirection] = None

    def getExit(self, direction):
        """
        Returns a reference to an adjacent space.
        Returns None if no space exists in given direction.

        @param direction:   Direction of adjacent space.
                            Must be one of the directions defined in
                            constants.Direction.
        
        @return:            Reference to space in given direction.
                            (Returns None if no exit is defined
                            for given direction).
        """
        space = self._exits[direction]
        return space

    def _isExit(self, exit):
        """
        Makes sure that a string represents a valid exit.

        @param direction:   Name of exit.

        @return:            True if valid exit, False otherwise.
        """
        availableExits = self._exits.keys()
        if exit not in availableExits:
            return False
        return True

    def _oppositeDirection(self, direction):
        """
        Returns the opposite direction. (e.g. North is opposite of South)

        @param direction:   A direction (from constants.Direction)
        
        @return:            Opposite direction (from constants.Direction)
        """
        if direction == Direction.NORTH:
            return Direction.SOUTH
        elif direction == Direction.SOUTH:
            return Direction.NORTH
        elif direction == Direction.EAST:
            return Direction.WEST
        elif direciton == Direction.WEST:
            return Direction.EAST
        else:
            raise AssertionError("Not a valid direction: %s" % direction)
