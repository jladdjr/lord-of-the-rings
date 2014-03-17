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
        self._shire  = Space("Shire", "Home of Hobbits.")
        self._gondor = Space("Gondor", "Capital: Osgiliath.")
        self._mordor = Space("Mordor", "Home of Sauron.")

        #TODO: These Spaces need to be connected together
        #      (once Dmitriy's code has been merged with this code) -JDL

        #TODO: Need to create a getWorld() method 
