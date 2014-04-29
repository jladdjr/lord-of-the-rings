#!/usr/bin/python

from command import Command
from space import Space
from player import Player
from cities.city import City

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
        description = location.getDescription()
        items = location.getItems()
        itemsList = items.getItems()
        
        #Give space name and description
        print "%s: %s" % (locationName, description)

        #If space contains a city/cities
        if location.getCity():
            city = location.getCity()
            #For single cities...
            if isinstance(city, City):
                cityName = city.getName()
                cityDescription = city.getDescription()
                print "%s is contained in %s." % (cityName, locationName)
                print "%s: %s" % (cityName, cityDescription)
            #For multiple cities...
            if isinstance(city, list):
                for specificCity in city:
                    cityName = specificCity.getName()
                    cityDescription = specificCity.getDescription()
                    print "%s is contained in %s." % (cityName, locationName)
                    print "%s: %s" % (cityName, cityDescription) 
     
        #If space has one or more uniquePlace objects
        if location.getUniquePlace():
            uniquePlace = location.getUniquePlace()
            uniquePlaceName = uniquePlace.getName()
            uniquePlaceDescription = uniquePlace.getDescription()
            print "%s is contained in %s." % (uniquePlaceName, locationName)
            print "%s: %s" % (uniquePlaceName, uniquePlaceDescription)
   
        #If space has items
        if len(itemsList) > 0:
            print "\nItems contained in %s:" % locationName
            for item in itemsList:
                print "\t%s" % item.getName()
