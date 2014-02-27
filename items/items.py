#!/usr/bin/python

from items.item import Item

class Items(object):
    """
    A simple collection of items.
    """

    def __init__(self, itemSet=None):
        """
        Initialize an Items object.

        @keyword itemSet:     (Optional) A single Item object or a
                               list of Item objects.
        """
        self._items = []
        self._weight = 0

        #Received single item
        if isinstance(itemSet, Item):
            self._items.append(itemSet)
            self._weight += itemSet.getWeight()
        #Received set of items
        elif isinstance(itemSet, list):
            for item in itemSet:
                if not isinstance(item, Item):
                    errorMsg = "Items initialized with list containing non-Item object(s)."
                    raise AssertionError(errorMsg)
                self._items.append(item)
                self._weight += item.getWeight()

    def addItem(self, item):
        """
        Adds an item.

        @param item:    An item.
        """
        #Check preconditions
        if not isinstance(item, Item):
            errorMsg = "Items.addItem() passed non-Item object."
            raise AssertionError(errorMsg)

        self._items.append(item)
        self._weight += item.getWeight()

    def removeItem(self, item):
        """
        Removes an item.

        @param item:    An item in this collection.
        """
        self._items.remove(item)
        self._weight -= item.getWeight()
   
    def containsItem(self, item):
        """
        Determines if item is contained in this collection.

        @param item:    An item.
        @return:        True if item is in this collection, False otherwise.
        """
        return (item in self._items)

    def count(self):
        """
        Returns the number of items.

        @return:    Number of items.
        """
        return len(self._items)

    def weight(self):
        """
        Determines total weight of items.

        @return: Total weight of items.
        """
        return self._weight 
 
    def __iter__(self):
        """
        Provide an iterator for this set of items.


        Allows you to create for loops using Items objects:


            >>> from item import Item
            >>> from items import Items
            >>> item1 = Item("sword", "made by elves", 2)
            >>> item2 = Item("helmet", "made by men", 1)
            >>> item3 = Item("healing potion", "restores health", 1)
            >>> myItems = Items([item1, item2, item3])
            >>> for item in myItems:
            ...     print item.getName()
            ... 
            sword
            helmet
            healing potion


        """
        return iter(self._items)
