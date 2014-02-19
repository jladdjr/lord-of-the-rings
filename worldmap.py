#!/usr/bin/python

from space import Space

class WorldMap(object):
    """
    The map of middle earth made up of a collection of spaces."
    """

    def __init__(self):
        """
        Instantiates the spaces that make up the world map.
        """
        ###Space needs a way to have space-specific paramaters from its __init__###
        self._shire = Space()
        self._mordor = Space()

        self._worldMap = [self._shire, self._mordor]

        pass
