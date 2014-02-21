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
        
        self._shire = Space("Shire")
        self._gondor = Space("Gondor")
        self._mordor = Space("Mordor")

        self._worldMap = [self._shire, self._gondor, self._mordor]
