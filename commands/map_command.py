#!/usr/bin/python

from command import Command
from cities.city import City
from unique_place import UniquePlace
import constants

class MapCommand(Command):
    """
    Map command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new Map command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Runs Map Command. If player may move to any of the four cardinal
        directions, the space corresponding to that direction is directed
        to self._printInformation().
        """        
        #Generate variables for map locations
        location = self._player.getLocation()
        exits = location.getExits()

        print "Your map is more a set of notes and instructions...."
        print ""
        print "From %s, you may go to the following:" % location.getName()
        
        #List details for each space in NSEW order
        if exits[constants.Direction.NORTH]:
            space = exits[constants.Direction.NORTH]
            self._printInformation(space, constants.Direction.NORTH)
        if exits[constants.Direction.SOUTH]:
            space = exits[constants.Direction.SOUTH]
            self._printInformation(space, constants.Direction.SOUTH)
        if exits[constants.Direction.EAST]:
            space = exits[constants.Direction.EAST]
            self._printInformation(space, constants.Direction.EAST)
        if exits[constants.Direction.WEST]:
            space = exits[constants.Direction.WEST]
            self._printInformation(space, constants.Direction.WEST)
            
    def _printInformation(self, space, direction):
        """
        Prints the name of the space and any cities and unique places
        that it may have.
        
        @param space:               The space that is currently being 
                                    detailed.
        @param direction:           The direction of the space with 
                                    respect to player's current location.
        """
        #For current space
        spaceName = space.getName()
        print "\tTo the %s: %s." % (direction, spaceName)
        
        #If a city/cities exist for a particular space
        if space.getCity():
            cities = space.getCity()
            if isinstance(cities, City):
                cityName = cities.getName()
                print "\t--%s is in %s." % (cityName, spaceName)
            elif isinstance(cities, list):
                for city in cities:
                    cityName = city.getName()
                    print "\t--%s is in %s." % (cityName, spaceName)
                    
        #If a unique place/unique places exist for a particular space
        if space.getUniquePlace():
            uniquePlaces = space.getUniquePlace()
            if isinstance(uniquePlaces, UniquePlace):
                uniquePlaceName = uniquePlaces.getName()
                print "\t--%s is in %s." % (uniquePlaceName, spaceName)
            elif isinstance(uniquePlaces, list):
                for uniquePlace in uniquePlaces:
                    uniquePlaceName = uniquePlace.getName()
                    print "\t--%s is in %s." % (uniquePlaceName, spaceName)
        print ""