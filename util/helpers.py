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

    charmNames.sort()
    for charmName in charmNames:
        sortedItems.append(charms[charmName])

    items.clearItems()
    items.addItems(sortedItems)