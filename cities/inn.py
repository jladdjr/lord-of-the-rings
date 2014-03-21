#!/usr/bin/python

class Cities(object):
    """
    Inns are in cities. Inns allow player to heal.
    """
    def __init__(self, player, name, description, greetings, talk):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters a inn.
        @param talk:           What the local say when the user talks to the locale.
        """
        self._player = player
        
        self._name = name
        self._description = description
        self._greetings = greetings
        self._talk = talk

    def getName(self):
        """
        Returns name of inn.

        @return:    The name of the inn.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of inn.

        @return:    The description of the inn.
        """
        return self._description

    def Greetings(self):
        """
        Prints a screen that represents a player greeting upon entering inn.
        """
        print self._greetings
        
    def Talk(self):
        """
        Prints a string that represents what happens when player attempts to talk to the locale.
        """
        print self._talk

    def Heal(self):
        """
        Heals player.
        """
        
