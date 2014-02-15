#!/usr/bin/python

from item import Item

class Items(object):
    """
    A simple collection of items.
    """

    def __init__(self):
        """
        Initialize an Items object.
        """
        self._items = []

    def addItem(self, item):
        """
        Adds an item.

        @param item:    An item.
        """


