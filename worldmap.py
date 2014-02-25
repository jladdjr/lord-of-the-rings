#!/usr/bin/python

from space import Space

class WorldMap(object):
    """
    Instantiates the spaces that make up the game map.
    """
    
    def __init__(self):
        """
        Instantiates the spaces that make up the world map.
        """
        self._shire = Space("Shire")
        self._gondor = Space("Gondor")
        self._mordor = Space("Mordor")
