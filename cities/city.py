#!/usr/bin/python

from place import Place
from cities.building import Building
import pdb

class City(Place):
    """
    Cities inherit from the Place parent class.
    Cities are the towns of the game. Cities may have inns, blacksmiths and people to talk to.
    """
    def __init__(self, name, description, greetings, buildings = None):
        """
        Initializes city object.

        @param name:           The name of the city.
        @param description:    A description of the city.
        @param greetings:      The greetings the user gets as he enters a city.
        @param buildings:      A list of the buildings in city.
        """
        self._name = name
        self._description = description
        self._greetings = greetings
        self._buildings = buildings

    def greetings(self):
        """
        Prints a screen that represents a player greeting upon entering city.
        """
        return self._greetings
        
    def getBuildings(self):
        """
        Returns list of building objects.
        """
        return self._buildings

    def getBuildingString(self, string):
        """
        Returns building object given string parameter.

        @param:    Name of the building
        """
        for building in self._buildings:
            if building.getName() == string:
                return building
    def createDictionaryOfBuildings(self):
        """
        Creates a dictionary of building objects. The keys are the building name that references the building object.
        """
        
        dictionary = {}
        #if there is 1 building
        if isinstance(self._buildings, Building):
            dictionary[self._buildings.getName()] = self._buildings
        #if there are multiple buildings
        elif isinstance(self._buildings,list):
            for building in self._buildings:
                dictionary[building.getName()] = building
        return dictionary
    
    def enter(self, player):  
        print "Entering %s" % self._name
        print "\n %s \n" % self._description
        print "You have found the following:"
        
        #if there is 1 building
        if isinstance(self._buildings,Building):
            print "\t %s" % self._buildings.getName()
        #if there are multiple buildings
        elif isinstance(buildings,list):
            for building in self._buildings:
                print "\t %s" % self._building.getName()
            
        dictionary = self.createDictionaryOfBuildings()        
        
        #pdb.set_trace()
        print "If you would like to go to one of these, then type the name. Otherwise, type 'leave city'"
        command = raw_input("What would you like to do?")
        
        while (command not in dictionary.keys()) or (command == 'leave city'):
            if command == 'leave city':
                break
            else:
                print "I did not recognize that. Try again. \n"
                command = raw_input("What would you like to do? \n")
        else:
            dictionary[command].enter(player)
