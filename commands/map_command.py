#!/usr/bin/python

from command import Command
from cities.city import City
from unique_place import UniquePlace

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
        Run Map command.
        """        
        #Generate variables for map locations
        location = self._player.getLocation()
        exits = location.getExits()

        print "Your map is more a set of notes and instructions...."
        print ""
        print "From %s, you may go to the following:" % location.getName()

        for direction in exits:
            self._printInformation(direction)
            
    def _printInformation(self, direction):
        location = self._player.getLocation()
        exits = location.getExits()

        #If a space exists for a particular location
        if exits[direction]:
            space = exits[direction]
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
                        cityName = cities.getName()
                        print "\t--%s is in %s." % (cityName, spaceName)
                        
            #If a unique place/unique places exist for a particular space
            if space.getUniquePlace():
                uniquePlaces = space.getUniquePlace()
                if isinstance(uniquePlaces, UniquePlace):
                    uniquePlaceName = uniquePlaces.getName()
                    print "\t--%s is in %s." % (uniquePlaceName, spaceName)
                elif isinstance(uniquePlaces, list):
                    for uniquePlace in uniquePlaces:
                        uniquePlaceName = uniquePlaces.getName()
                        print "\t--%s is in %s." % (uniquePlaceName, spaceName)
            print ""
