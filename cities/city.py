#!/usr/bin/python

from place import Place
from cities.building import Building

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
        @param greetings:      The greetings the user gets as he enters the city.
        @param buildings:      A list of the buildings in the city.
        """
        self._name = name
        self._description = description
        self._greetings = greetings
        self._buildings = buildings

    def greetings(self):
        """
        Returns the string that represents a player greeting upon entering the city.
        """
        return self._greetings
        
    def getBuildings(self):
        """
        Returns the list of building objects.
        """
        return self._buildings

    def getBuildingString(self, string):
        """
        Returns building object given string parameter.

        @param:    Name of the building.
        """
        for building in self._buildings:
            if building.getName() == string:
                return building
    
    def createDictionaryOfBuildings(self):
        """
        Creates a dictionary of building objects. The keys are the building name that references the building object.
        """
        
        dictionary = {}
        buildings = self.getBuildings()
        #if there is 1 building
        if isinstance(buildings, Building):
            dictionary[buildings.getName()] = buildings
        #if there are multiple buildings
        elif isinstance(buildings,list):
            for building in buildings:
                dictionary[building.getName()] = building
        return dictionary
    
    def printBuildings(self):
        """
        The method for printing buildings in the city
        """
        
        buildings = self.getBuildings()
        #If there is 1 building
        if isinstance(buildings, Building):
            print "\t %s\n" % buildings.getName()
        #If there are multiple buildings
        elif isinstance(buildings, list):
            for building in buildings:
                print "\t %s" % building.getName()
            print"\n"
    
    def enter(self, player):  
        """
        The method for entering the buildings in the city.
        @param: player       The current player
        """

        buildingDictionary = self.createDictionaryOfBuildings()

        print "Entering %s" % self.getName()
        print "\n %s \n" % self.getDescription()

        while True:
            print "You have found the following:"
            
            #Print list of buildings
            self.printBuildings()
            
            print "To go to a building type its name. Otherwise, type 'leave city'"
            command = raw_input("Where would you like to go?\n")
            
            #If player chooses to leave the city
            if command == 'leave city':
                print "Leaving %s.\n" % self.getName()
                return
            #If player selects something other than to leave the city
            while True:
                if command in buildingDictionary.keys():
                    #Enter building
                    buildingDictionary[command].enter(player)
                    #Player has left building, and chooses what to do next
                    print "\nYou are now back in %s." % self.getName()
                    break
                else:
                    print "\nI did not recognize %s. Try again." % command
                    break

