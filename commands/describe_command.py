#!/usr/bin/python

from command import Command
from space import Space
from player import Player
from cities.city import City
from unique_place import UniquePlace

import pdb

class DescribeCommand(Command):
    """
    Describe the current space.
    """

    def __init__(self, name, explanation, player):
        """
        Initializes new describe command.
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
        city = location.getCity()
        uniquePlace = location.getUniquePlace()
        
        #Give space name and description
        print "%s: %s." %(locationName, description)

        #pdb.set_trace()
        #If space has one city:
        if isinstance(city,City):
            cityName = city.getName()
            print "\n%s is contained in %s" %(cityName, locationName)
        
        #if space has multiple cities (and the variable city is actually a list of cities):
        elif isinstance(city,list):
            for eachCity in city:
                eachCityName = eachCity.getName()
                print "\n%s is contained in %s." %(eachCityName, locationName)

        #If space has one uniquePlace object
        if isinstance(uniquePlace, UniquePlace):
            uniquePlaceName = uniquePlace.getName() 
            print "\n%s is contained in %s." %(uniquePlaceName, locationName)           
        
        #if space has multiple uniquePlaces (the the variable uniquePlace is actually a list of uniquePlaces)
        if isinstance(uniquePlace, list):
            for eachUniquePlace in uniquePlace:
                eachUniquePlaceName = eachUniquePlace.getName()
                print "\n%s is contained in %s." %(eachUniquePlaceName, locationName)
        
        #If space has items
        if len(itemsList) > 0:
            print "\nItems contained in %s:" %locationName
            for item in itemsList:
                print "\t%s" %item.getName()
