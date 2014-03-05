#!/usr/bin/python

"""
Player's starting inventory. 
"""

#This should be handled by a GameLoader class instead of here.

#This list contains multiple references to the *same* objects. In reality, there is only one steelDagger and one leatherCloak being used in this list.

startingInventory = [uniqueitems.steelDagger, uniqueitems.steelDagger, uniqueitems.leatherCloak, uniqueitems.leatherCloak, uniqueitems.leatherCloak]
