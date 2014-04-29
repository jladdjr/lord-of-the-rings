#!/usr/bin/python

from place import Place

class City(Place):
    """
    Cities are the towns of the game. Cities may have inns, blacksmiths and people to talk to.
    """
    def __init__(self, name, description, greeting, buildings = None):
        """
        Initializes city object.

        @param name:           The name of the city.
        @param description:    A description of the city.
        @param greeting:       The greeting the user gets as he enters the city.
        @param buildings:      A list of the buildings in the city.
        """
        Place.__init__(self, name, description, greeting)

        self._buildings = buildings
        
    def returnCity(self, name):
        """
        Returns the city object, given the name of the city.
        
        @param name:    The name of city.
        
        @return:        The city object.
        """
        if name == self._name:
            return self
            
        return None
        
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
        else:
            return None
