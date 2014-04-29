#!/usr/bin/python

from constants import Direction
from items.item_set import ItemSet

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """
    def __init__(self, name, description, items = None, city = None, uniquePlace = None):
        """
        Initialize a Space object.

        @param name:            Name of space.
        @param description:     Description of space.

        @keyword items:         (Optional) Items found in the space.
                                May be a reference to a single item or an ItemSet.
        @keyword city:          (Optional) Reference to the city objects in space.
                                May be a reference to an object or a list.
        @keyword uniquePlace:  (Optional) Reference to the unique places in Middle Earth. 
                                May be a reference to an object or a list.

        """
        self._exits = { Direction.NORTH : None,
                        Direction.SOUTH : None,
                        Direction.EAST : None,
                        Direction.WEST : None }

        self._name = name
        self._description = description
        #TODO: Need to add items passed into method; items is currently ignored.
        #      Will need to check if items refers to single object or to an ItemSet.
        #      If it points to an ItemSet, you can just set self._items to that ItemSet. 
        #      (self._items = items)
        self._items = ItemSet()
        self._city = city
        self._uniquePlace = uniquePlace

    def getName(self):
        """
        Returns the name of the room.

        @return:    Name of the room.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of the room.

        @return:    Description of room.
        """
        return self._description
        
    def getItems(self):
        """
        Returns a string of times.

        @return:    Items in Space (as ItemSet).
        """
        return self._items
        
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

        @return:    True if item is contained in Space, False otherwise.
        """
        return self._items.containsItem(item)

    def containsItemString(self, string):
        """
        Determines if room contains an item.

        @param item:     The string associated with the name of the item that we are looking for.

        @return:    True if item is contained in Space, False otherwise.
        """
        #TODO: Use ItemSet's containsItemWithName() instead here. 

        for item in self._items:
            if item.getName() == string:
                return True
            
        return False
    
    def getCity(self):
        """
        Returns city object.

        @return:    Reference to cit(ies).
                    May be reference to single city or list of cities.
        """
        return self._city

    def getUniquePlace(self):
        """
        Returns uniquePlace object(s).

        @return:    Reference to unique place(s).
                    May be reference to single unique place or list of unique places.
        """
        return self._uniquePlace

    def createExit(self, direction, space, outgoingOnly = False):
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

    def getExits(self):
        """
        Returns dictionary of direction-space pairs.

        @return:            Dictionary of direction-space pairs.
        """
        return self._exits

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
