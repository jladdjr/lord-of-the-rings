#!/usr/bin/python

from command import Command
from cities.city import City

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
        locationName = location.getName()
        exits = location.getExits()

        cities = {"north": None, "south": None, "east": None, "west": None}
        uniquePlaces = {"north": None, "south": None, "east": None, "west": None}

        if exits["north"]:
            north = exits["north"]
            northName = north.getName()
            if north.getCity():
                northCity = north.getCity()
                cities["north"] = northCity
                if isinstance(northCity, City):
                    northCityName = northCity.getName()
            if north.getUniquePlace():
                northUniquePlace = north.getUniquePlace()
                uniquePlaces["north"] = northUniquePlace
                northUniquePlaceName = northUniquePlace.getName()
        if exits["south"]:
            south = exits["south"]
            southName = south.getName()
            if south.getCity():
                southCity = south.getCity()
                cities["south"] = southCity
                if isinstance(southCity, City):
                    southCityName = southCity.getName()
            if south.getUniquePlace():
                southUniquePlace = south.getUniquePlace()
                uniquePlaces["south"] = southUniquePlace
                southUniquePlaceName = southUniquePlace.getName()
        if exits["east"]:
            east = exits["east"]
            eastName = east.getName()
            if east.getCity():
                eastCity = east.getCity()
                cities["east"] = eastCity
                if isinstance(eastCity, City):
                    eastCityName = eastCity.getName()
            if east.getUniquePlace():
                eastUniquePlace = east.getUniquePlace()
                uniquePlaces["east"] = eastUniquePlace
                eastUniquePlaceName = eastUniquePlace.getName()
        if exits["west"]:
            west = exits["west"]
            westName = west.getName()
            if west.getCity():
                westCity = west.getCity()
                cities["west"] = westCity
                if isinstance(westCity, City):
                    westCityName = westCity.getName()
            if west.getUniquePlace():
                westUniquePlace = west.getUniquePlace()
                uniquePlaces["west"] = westUniquePlace
                westUniquePlaceName = westUniquePlace.getName()
        
        #Print map
        print "Your map a more a set of notes and instructions...."
        print ""
        print "From %s, you may go to the following:" % locationName
        
        if exits["north"]:
            north = exits["north"]
            print "\tTo the North: %s." % northName
            if cities["north"]:
                if isinstance(cities["north"], City):
                    print "\t--%s is in %s." % (northCityName, northName)
                elif isinstance(cities["north"], list):
                    for city in cities["north"]:
                        print "\t--%s is in %s." % (city.getName(), northName)
            if uniquePlaces["north"]:
                print "\t--%s is in %s." % (northUniquePlaceName, northName)
            print ""
        if exits["south"]:
            south = exits["south"]
            print "\tTo the South: %s." % southName
            if cities["south"]:
                if isinstance(cities["south"], City):
                    print "\t--%s is in %s." % (southCityName, southName)
                elif isinstance(cities["south"], list):
                    for city in cities["south"]:
                        print "\t--%s is in %s." % (city.getName(), southName)
            if uniquePlaces["south"]:
                print "\t--%s is in %s." % (southUniquePlaceName, southName)
            print ""
        if exits["east"]:
            east = exits["east"]
            print "\tTo the East: %s." % eastName
            if cities["east"]:
                if isinstance(cities["east"], City):
                    print "\t--%s is in %s." % (eastCityName, eastName)
                elif isinstance(cities["east"], list):
                    for city in cities["east"]:
                        print "\t--%s is in %s." % (city.getName(), eastName)
            print ""
        if exits["west"]:
            west = exits["west"]
            print "\tTo the West: %s." % westName
            if cities["west"]:
                if isinstance(cities["west"], City):
                    print "\t--%s is in %s." % (westCityName, westName)
                elif isinstance(cities["west"], list):
                    for city in cities["west"]:
                        print "\t--%s is in %s." % (city.getName(), westName)
            print ""
