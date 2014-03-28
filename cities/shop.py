#!/usr/bin/python

from building import Building
import factories.shop_factory

class Shop(Building):
    """
    Shops are buildings that allow player to buy items.
    """
    def __init__(self, name, description, greetings, numItems, quality):
        """
        Initializes shop object.

        @param name:           The name of the shop.
        @param description:    A description of the shop.
        @param greetings:      The greetings the user gets as he enters a shop.
        @param numItems:       The number of items that can be bought at the shop.
        @apram quality:        The quality (0-100) of the shop. The higher the quality, the more effective the items that can be bought at this shop.
        """
        Buildings.__init__(self, name, description, greetings)
        
        self._numItems = numItems
        self._quality = quality
        self._items = shop_factory.getItems(numItems, quality)

    def getItems(self, numItems, quality):
        """
        Returns the items in the shop.
        """
        return self._items
        
