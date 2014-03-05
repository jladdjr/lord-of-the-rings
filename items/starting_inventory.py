#!/usr/bin/python

from items import unique_items

"""
Player's starting inventory. 
"""

#This should be handled by a GameLoader class instead of here.

#This list contains multiple references to the *same* objects. In reality, there is only one steelDagger and one leatherCloak being used in this list.

startingInventory = [unique_items.steelDagger, unique_items.steelDagger, unique_items.leatherCloak, unique_items.leatherCloak, unique_items.leatherCloak]
