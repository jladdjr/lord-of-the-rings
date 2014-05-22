#!/usr/bin/python

from command import Command
from space import Space
from player import Player
from cities.city import City
from unique_place import UniquePlace


class DescribeCommand(Command):
    """
    Describes the current space.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new describe command.

        @param name:         The name of player.
        @param explanation:  Explanation of player.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)
        
        self._player = player

    def execute(self):
        """
        Runs Describe command.
        """
        location = self._player.getLocation()
        locationName = location.getName()
        locationDescription = location.getDescription()
        items = location.getItems()
        itemsList = items.getItems()
        city = location.getCity()
        uniquePlace = location.getUniquePlace()
        
        #Give space name and locationDescription
        print "%s: %s" % (locationName, locationDescription)

        #If there are no cities or uniquePlaces in this space
        if not city and not uniquePlace:
            print "%s has no places for you to enter!" % locationName

        #If there is at least 1 city or uniquePlace
        else:
            print "The following are contained in %s:" % locationName

            #If space has one city:
            if isinstance(city, City):
                cityName = city.getName()
                print "\t%s" % cityName
            
            #If space has multiple cities (and the variable city is actually a list of cities):
            elif isinstance(city, list):
                for eachCity in city:
                    eachCityName = eachCity.getName()
                    print "\t%s" % eachCityName

            #If space has one uniquePlace object
            if isinstance(uniquePlace, UniquePlace):
                uniquePlaceName = uniquePlace.getName() 
                print "\t%s" % uniquePlaceName           
            
            #If space has multiple uniquePlaces (the the variable uniquePlace is 
            #actually a list of uniquePlaces)
            if isinstance(uniquePlace, list):
                for eachUniquePlace in uniquePlace:
                    eachUniquePlaceName = eachUniquePlace.getName()
                    print "\t%s" % eachUniquePlaceName
        
        #If space has items
        if len(itemsList) > 0:
            print "\nItems contained in %s:" % locationName
            for item in itemsList:
                print "\t%s" % item.getName()
