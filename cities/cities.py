#!/usr/bin/python

class Cities(object):
    """
    Cities are the towns of the game. Cities may have inns, blacksmiths and people to talk to.
    """
    def __init__(self, name, description, greetings, talk):
        """
        Initializes city object.

        @param name:           The name of the city.
        @param description:    A description of the city.
        @param greetings:      The greetings the user gets as he enters a city.
        @param talk:           What the local say when the user talks to the locale.
        """
        self._name = name
        self._description = description
        self._greetings = greetings
        self._talk = talk

    def getName(self):
        """
        Returns name of city.

        @return:    The name of the city.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of city.

        @return:    The description of the city.
        """
        return self._description

    def Greetings(self):
        """
        Prints a screen that represents a player greeting upon entering city.
        """
        print self._greetings
        
    def Talk(self):
        """
        Prints a string that represents what happens when player attempts to talk to the locale.
        """
        print self._talk
