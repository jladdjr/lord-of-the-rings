#!/usr/bin/python

from place import Place
from cities.building import Building

class City(Place):
    """
    Cities inherit from Place.
    
    Cities serve as the towns of the game. Cities may have inns, blacksmiths
    and squares.
    """
    def __init__(self, name, description, greetings, buildings = None):
        """
        Initializes the city.

        @param name:           The name of the city.
        @param description:    A description of the city.
        @param greetings:      The greetings the user gets as he enters the 
                               city.
        @param buildings:      A list of the buildings in the city.
        """
        #Call parent's init method
        Place.__init__(self, name, description, greetings)
        
        self._buildings = buildings

    def getGreetings(self):
        """
        Returns the string that represents player greeting upon entering
        the city.

        @return:    The string displayed upon entering a city.
        """
        return self._greetings
        
    def getBuildings(self):
        """
        Returns the list of building objects.

        @return:    List of building objects.
        """
        return self._buildings

    def getBuildingString(self, string):
        """
        Returns the building object matching its name.

        @param string:    The name of the building.
        
        @return:          Either the building object if the object is found or
                          None otherwise.
        """
        for building in self._buildings:
            if building.getName() == string:
                return building
        else:
            return None
    
    def _createDictionaryOfBuildings(self):
        """
        Creates a dictionary of building objects. Name-pairs are 
        building names and the objects they correspond to.
        
        @return:    A dictionary of buildings name and their 
                    corresponding objects.
        """
        buildingDictionary = {}
        buildings = self.getBuildings()
        #If there is one building
        if isinstance(buildings, Building):
            buildingDictionary[buildings.getName()] = buildings
        #If there are multiple buildings
        elif isinstance(buildings, list):
            for building in buildings:
                buildingDictionary[building.getName()] = building
                
        return buildingDictionary
    
    def _printBuildings(self):
        """
        Helper method that prints the building contained in city.
        """
        buildings = self.getBuildings()
        #If there is one building
        if isinstance(buildings, Building):
            print "\t%s" % buildings.getName()
        #If there are multiple buildings
        elif isinstance(buildings, list):
            for building in buildings:
                print "\t%s" % building.getName()
        print ""
        
    def enter(self, player):  
        """
        The action sequence for city.

        @param player:       The current player
        """
        buildingDictionary = self._createDictionaryOfBuildings()

        print "Entering %s!" % self.getName()
        print "\n%s" % self.getDescription()
        print "%s" % self.getGreetings()
        print ""
        raw_input("Press enter to continue. ")
        print ""
        
        while True:
            print "You have found the following:"
            
            #Print list of buildings
            self._printBuildings()
            
            print "To go to a building type its name. Otherwise, type 'leave'"
            command = raw_input("Where would you like to go?\n")
            
            #If player chooses to leave the city
            if command == 'leave':
                print ""
                print "Leaving %s." % self.getName()
                return
                
            #For other choices
            if command in buildingDictionary.keys():
            
                #Enter building
                buildingDictionary[command].enter(player)
                
                #Prompt for next action
                print "\nYou are now back in %s." % self.getName()
                print ""
            else:
                print "\nI did not recognize %s. Try again.\n" % command