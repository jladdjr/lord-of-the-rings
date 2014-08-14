#!/usr/bin/python

from command import Command
from space import Space
from cities.city import City
from unique_place import UniquePlace
import constants

class MapCommand(Command):
    """
    Map command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes Map command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Calls self._printInformation on each of the spaces that are connected
        to the player's current space.
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
            #For single spaces
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.NORTH)
            #For lists of spaces
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, 
                        constants.Direction.NORTH)
                        
        if exits[constants.Direction.SOUTH]:
            space = exits[constants.Direction.SOUTH]
            #For single spaces
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.SOUTH)
            #For lists of spaces
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, 
                        constants.Direction.SOUTH)
                        
        if exits[constants.Direction.EAST]:
            space = exits[constants.Direction.EAST]
            #For single spaces
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.EAST)
            #For lists of spaces
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, 
                        constants.Direction.EAST)
                        
        if exits[constants.Direction.WEST]:
            space = exits[constants.Direction.WEST]
            #For single spaces
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.WEST)
            #For lists of spaces
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, 
                        constants.Direction.WEST)
            
    def _printInformation(self, space, direction):
        """
        Prints the name of the space and lists any cities and unique places
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