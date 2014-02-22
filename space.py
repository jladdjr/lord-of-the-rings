#!/usr/bin/python

<<<<<<< HEAD
from constants import Direction
=======
from items import Items
>>>>>>> master

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """

    def __init__(self):
        """
<<<<<<< HEAD
        Initialize space object.
        """
        self._exits = { Direction.North : None,
                        Direction.South : None,
                        Direction.East  : None,
                        Direction.West  : None }

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
        if direction == Direction.North:
            return Direction.South
        elif direction == Direction.South:
            return Direction.North
        elif direction == Direction.East:
            return Direction.West
        elif direciton == Direction.West:
            return Direction.East
        else:
            raise AssertionError("Not a valid direction: %s" % direction)

=======
        Intialize a Space object.
        """
        self._items = Items()

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
        return self._items.containsItem(item)

    def getItems(self):
        """
        Returns items contained by room.
        (i.e. An Items object).
        
        @return: An Items object containing 
        set of items found in room.
        """
        return self._items
>>>>>>> master
