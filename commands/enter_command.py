#!/usr/bin/python

from command import Command
from cities.city import City
from unique_place import UniquePlace

class EnterCommand(Command):
    """
    Allows player to enter a city or unique place.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, True)

        self._player = player
    
    def _displayPlacesToEnter(self):
        """
        Displays the possible places (Cities or UniquePlaces) that player may enter.
        """
        playerName = self._player.getName()
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #If there are no cities or unique places
        if not (city or uniquePlace):
            print "No places to enter."
        #Otherwise print the possible places to enter
        else:
            if isinstance(city, City):
                print "%s may enter the following city:" % playerName
                print "\t%s" % city.getName()
            elif isinstance(city, list):
                print "%s may enter the following cities:" % playerName
                for eachCity in city:
                    print "\t%s" % eachCity.getName()

        #Display uniquePlaces that player may enter
            if isinstance(uniquePlace, UniquePlace):
                print "\t%s" % uniquePlace.getName()
            elif isinstance(uniquePlace, list):
                for eachUniquePlace in uniquePlace:
                    print "\t%s" % eachUniquePlace.getName()
        print ""
        
    def _createDictionaryOfPlaces(self):
        """
        Creates a dictionary of places that are within the space. 
        The keys are the names of the places and reference the actual places. 
        """
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        dictionary = {}
        
        #Add cities to dictionary
        if isinstance(city, City):
            dictionary[city.getName()] = city
        elif isinstance(city, list):
            for eachCity in city:
                dictionary[eachCity.getName()] = eachCity
        
        #Add uniquePlaces to dictionary
        if isinstance(uniquePlace, UniquePlace):
            dictionary[uniquePlace.getName()] = uniquePlace
        elif isinstance(uniquePlace, list):
            for eachUniquePlace in uniquePlace:
                dictionary[eachUniquePlace.getName()] = eachUniquePlace
        
        return dictionary
    
    def execute(self):
        """
        Allows player to enter a city or uniquePlace.
        """
        #Show the places that player may enter
        self._displayPlacesToEnter()
        
        #Create a dictionary of places within space. 
        #Keys are the names of places that reference the actual places
        dictionary = self._createDictionaryOfPlaces()
        
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()
        
        #If there is no place to enter
        if not (city or uniquePlace):
            return
        
        #Entering the place that the player chooses to enter
        placeToEnter = raw_input("Which of these would you like to enter?\n")
        while (placeToEnter not in dictionary.keys()) or placeToEnter == 'stop':
            if placeToEnter == 'stop':
                break 
            print "\nThat name does not match the names of any of the places here."
            print "Try again, or type 'stop' to stop entering a place.\n"
            placeToEnter = raw_input("Which of these would you like to enter?\n")
        else:
            print "\n"
            dictionary[placeToEnter].enter(self._player)
