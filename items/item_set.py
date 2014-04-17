#!/usr/bin/python

from items.item import Item

class ItemSet(object):
    """
    A simple collection of items.
    """
    def __init__(self, itemSet=None):
        """
        Initialize an ItemSet object.

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
                    errorMsg = "ItemSet initialized with list containing non-Item object(s)."
                    raise AssertionError(errorMsg)
                self._items.append(item)
                self._weight += int(item.getWeight())

    def addItem(self, item):
        """
        Adds an item.

        @precondition: Item's name must not be used
        by any items already contained in ItemSet.

        @param item:    An item.
        """
        #Check preconditions
        if not isinstance(item, Item):
            errorMsg = "ItemSet.addItem() passed non-Item object."
            raise AssertionError(errorMsg)

        self._items.append(item)
        self._weight += int(item.getWeight())

    def getItems(self):
        """
        Returns list of items contained by ItemSet.

        @return:     List of items contained by ItemSet.
        """
        return self._items

    def getItemByName(self, name):
        """
        Gets an item with a given name.

        @param name:    Name of object.
        @return:        Item with given name.
                        Returns None if the item
                        cannot be found.
        """
        for item in self._items:
            if item.getName() == name:
                return item
        return None
    
    def removeItem(self, item):
        """
        Removes an item.

        @param item:    An item in this collection.
        """
        self._items.remove(item)
        self._weight -= int(item.getWeight())
   
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
        Provides an iterator for this set of items.
        """
        return iter(self._items)
