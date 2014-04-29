#!/usr/bin/python

class Place(object):
    """
    A  place on the map. Cities and Place inherit from this.
    """
    def __init__(self, name, description, greeting):
        """
        Initialize Place object.
        
        @param name:           The name of the Place.
        @param description:    A description of the Place.
        @param greetings:       The greeting upon entering Place.
        """
        self._name = name
        self._description = description
        self._greeting = greeting
    
    def getName(self):
        """
        Returns the name of Place.
        
        @return:    The name of the Place.
        """
        return self._name
        
    def returnPlace(self, name):
        """
        Returns the Place object.
        
        @param name:    The name of Place.
        
        @return:        The Place object.
        """
        if self._name == name:
            return self
            
        return None
        
    def getDescription(self):
        """
        Returns the description of Place.
        
        @return:    The description of Place.
        """
        return self._description
    
    def getGreeting(self):
        """
        Returns the greetings of Place
        """
        return self._greeting
    
    def enter(self):
        """
        The action sequence of Place. By default, does nothing.
        
        Child class should overwrite this method.
        """
        pass
