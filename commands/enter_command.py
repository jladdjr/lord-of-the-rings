#!/usr/bin/python

from command import Command
from cities.city import City
from unique_place import UniquePlace
import pdb

class EnterCommand(Command):
    """
    Allows player to enter a building.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player
    
    def displayPlacesToEnter(self):
        """
        Displays the possible places (Cities or uniquePlaces) that player may enter
        """
        name = self._player.getName()
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #if there are no cities or uniquePlaces
        if not (city or uniquePlace):
            print "No places to enter."
        #otherwise print the possible places to enter
        else:
            print "%s may enter the following cities:" % self._player.getName()
            if isinstance(city, City):
                print "\t%s" %city.getName()
            elif isinstance(city,list):
                for eachCity in city:
                    print "\t%s" %eachCity.getName()
                print ""

        #Display uniquePlaces that player may enter
            print "%s may also enter the following:" % self._player.getName()
            if isinstance(uniquePlace, UniquePlace):
                print "\t%s" %uniquePlace.getName()
            elif isinstance(uniquePlace,list):
                for eachUniquePlace in uniquePlace:
                    print "\t%s" %eachUniquePlace.getName()
                print ""
    def createDictionaryOfPlaces(self):
        """
        Creates a dictionary of places that are within the space. The keys are the names of the places and reference the actual places. 
        """
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        dictionary = {}
        
        #add cities to dictionary
        if isinstance(city,City):
            dictionary[city.getName()] = city
        elif isinstance(city,list):
            for eachCity in city:
                dictionary[eachCity.getName()] = eachCity
        
        #add uniquePlaces to dictionary
        if isinstance(uniquePlace,UniquePlace):
            dicitonary[uniquePlace.getName()] = uniquePlace
        elif isinstance(uniquePlace,list):
            for eachUniquePlace in uniquePlace:
                dictionary[eachUniquePlace.getName()] = eachUniquePlace
        
        return dictionary
        

    def execute(self):
        """
        Allows player to enter a building.
        """
        #pdb.set_trace()
        #show the places that player may enter
        self.displayPlacesToEnter()
        
        #create a dictionary of places within space. Keys are the names of places that reference the actual places
        dictionary = self.createDictionaryOfPlaces()
        
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #if there is no place to enter
        if not (city or uniquePlace):
            pass
        #entering the place that the player chooses to enter
        placeToEnter = raw_input("Which of these would you like to enter?\n")
        while (placeToEnter not in dictionary.keys()) or placeToEnter == 'stop':
            if placeToEnter == 'stop':
                break
            else: 
                print "\nThat name does not match the names of any of the places here. Try again, or type 'stop' to stop entering a place.\n"
            placeToEnter = raw_input("Which of these would you like to enter?\n")
        else:
            dictionary[placeToEnter].enter()
