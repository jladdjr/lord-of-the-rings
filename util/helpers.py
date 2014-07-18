#!/usr/bin/python

def generateMenu(prompt, options, appendQuit = False):
    """
    Generates menus and solicit and returns user choice.

    @param prompt:       User prompt. For example: "You are in the store."
    @param options:      List of options, stored as strings.
    @param appendQuit:   Whether there should be the option to quit.
    
    @return:             User choice.
     """
    print prompt
    print ""

    if appendQuit:
        options.append("Quit")

    index = 1
    for option in options:
        print "%s)\t%s" % (str(index), option) 
        index += 1

    choice = raw_input("Choice: ")

    return choice

def sortItems(items):
    """
    Sorts items in an ItemSet.
    
    @param items:   The ItemSet to sort.
    """
    #Import modules
    from items.weapon import Weapon
    from items.armor import Armor
    from items.charm import Charm
    from items.potion import Potion
    
    #Create variables
    itemsList = items.getItems()
    sortedItems = []
    
    charms = {}
    charmNames = []
    potions = {}
    potionNames = []
    
    #Weapon is first
    for item in itemsList:
        if isinstance(item, Weapon):
            sortedItems.append(item)
    
    #Armor is second
    for item in itemsList:
        if isinstance(item, Armor):
            sortedItems.append(item)
            
    #Sort charms by name
    for item in itemsList:
        if isinstance(item, Charm):
            charmName = item.getName()
            charmNames.append(charmName)
            charms[charmName] = item
            
    for item in itemsList:
        if isinstance(item, Potion):
            potionName = item.getName()
            potionNames.append(potionName)
            potions[potionName] = item

    charmNames.sort()
    for charmName in charmNames:
        sortedItems.append(charms[charmName])

    potionNames.sort()
    for potionName in potionNames:
        sortedItems.append(potions[potionName])
        
    items.clearItems()
    items.addItems(sortedItems)
    
def triangular(self, low, high, mode):
    """
    Generates a random number using a triangle distribution.
    
    @param low:     The bottom endpoint.
    @param high:    The top endpoint.
    @param mode:    The height of the triangle.
    
    @return:        The randomly generated number.
    """
    u = self.random()
    try:
        if mode is None:
            c = 0.5  
        else:
            c = (mode - low) / (high - low)
    except ZeroDivisionError:
        return low
        
    if u > c:
        u = 1.0 - u
        c = 1.0 - c
        low, high = high, low
    return low + (high - low) * (u * c) ** 0.5