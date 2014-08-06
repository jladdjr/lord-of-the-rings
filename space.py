#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from constants import Direction, RegionType
from items.unique_items import theOneRing

class Space(object):
    """
    A given location on the map. Connects with other spaces
    to form larger geographic areas.
    """
    def __init__(self, name, description, region, battleProbability = 0, 
    battleBonusDifficulty = 0, items = None, city = None, uniquePlace = None):
        """
        Initialize a Space object.

        @param name:                   Name of space.
        @param description:            Description of space.
        @param battleProbability:      Probability between [0, 1] that a 
                                       random battle will occur between 
                                       successive game command executions.
        @param battleBonusDifficulty:  Probability between [0, 1] that is used 
                                       to determine battle bonus difficulty. 
                                       This stat results in a percentage 
                                       increase over default monster stats and 
                                       number for any given space.
                                       
                                       For instance, if bonus difficulty is 
                                       set to .5, space will spawn 50% more 
                                       monsters with 150% base stats.
                                       
        @keyword items:                (Optional) Items found in the space.
                                       May be a reference to a single item or 
                                       an ItemSet.
        @keyword city:                 (Optional) City objects in space. May 
                                       be a reference to an individual object 
                                       or a list.
        @keyword uniquePlace:          (Optional) Reference to unique places 
                                       in space. May be a reference to an 
                                       individual object or a list.
        """
        self._exits = {Direction.NORTH : None,
                       Direction.SOUTH : None,
                       Direction.EAST : None,
                       Direction.WEST : None}

        self._name = name
        self._description = description
        self._region = region
        self._battleProbability = battleProbability
        self._battleBonusDifficulty = battleBonusDifficulty
        self._items = ItemSet()
        self._city = city
        self._uniquePlace = uniquePlace

    def getName(self):
        """
        Returns the name of the space.

        @return:    Name of the space.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of space.

        @return:    Description of space.
        """
        return self._description
        
    def getRegion(self):
        """
        Returns the region of the space.
        
        @return:    The region of space.
        """
        return self._region
        
    def getItems(self):
        """
        Returns a string of times.

        @return:    Items in Space (as ItemSet).
        """
        return self._items
        
    def addItem(self, item):
        """
        Adds an item to the space.

        @param item:    Item to add.
        """
        #Special prompt for theOneRing
        if item == theOneRing and self._name != "Orodruin":
            print "\nYou see some strange men walk by."
            return
            
        if isinstance(item, Item):
            self._items.addItem(item)
        elif isinstance(item, list):
            self._items.addItems(item)
        else:
            errorMsg = "space.AddItem() was given invalid item type."
            raise AssertionError(errorMsg)

    def removeItem(self, item):
        """
        Removes an item from the space.

        @param item:    Item to remove.
        """
        self._items.removeItem(item)

    def containsItem(self, item):
        """
        Determines if space contains an item.

        @param item:    Item object to search for.

        @return:    True if item is contained in 
                    Space, False otherwise.
        """
        return self._items.containsItem(item)

    def containsItemString(self, string):
        """
        Determines if space contains an item.

        @param string:   The name-string of 
                         the target item.

        @return:    True if item is contained 
                    in space, False otherwise.
        """ 
        return        self._items.containsItemWithName(string)
    
    def getCity(self):
        """
        Returns city object/objects.

        @return:    Reference to cit(ies).
                    May refer to a single city or list of cities.
        """
        return self._city

    def getUniquePlace(self):
        """
        Returns uniquePlace object(s).

        @return:    Reference to unique place(s).
                    May be reference to a single unique
                    place or a list of unique places.
        """
        return self._uniquePlace

    def getBattleProbability(self):
        """
        Returns probability of a random battle.

        @return:    The probability that a random
                    battle occurs.
        """
        return self._battleProbability

    def getBattleBonusDifficulty(self):
        """
        Returns bonus difficulty attribute of space.

        @return:    The difficulty parameter of space.
        """
        return self._battleBonusDifficulty

    def createExit(self, direction, space, outgoingOnly = False):
        """
        Create an exit to another space. By default,
        the method creates the appropriate exit
        in the second space. (This can be suppressed, 
        however, using I{outgoingOnly}).

        @param direction:       Direction of exit.
        @param space:           Adjacent space.
        @keyword outgoingOnly:  By default, this method creates the appropriate
                                exit in the second space. Set I{outgoingOnly}
                                to False to suppress this behaviour.
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
        the second space. (This can be suppressed, 
        however, using I{outgoingOnly}).

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
        elif direction == Direction.WEST:
            return Direction.EAST
        else:
            raise AssertionError("Not a valid direction: %s" % direction)