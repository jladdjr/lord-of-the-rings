#!/usr/bin/python

from cities.building import Building
import factories.shop_factory
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
from items.unique_items import theOneRing
from util.helpers import sortItems
import constants

class Shop(Building):
    """
    Shops inherit from Building.
    
    Shops serve as the markets of the game.
    """
    def __init__(self, name, description, greetings, region, numItems, 
        quality):
        """
        Initializes shop.

        @param name:        The name of the shop.
        @param description: The description of the shop.
        @param greetings:   The greetings the user gets as he enters a shop.
        @param region:      The region the shop is in.
        @param numItems:    The number of items that can be bought at the 
                            shop.
        @param quality:     The quality of the items that may be bought at 
                            shop.
                            Ranges from 1-20.
        """
        Building.__init__(self, name, description, greetings)

        #Create items attributes and generate items objects
        self._region = region
        self._numItems = numItems
        self._quality = quality
        
        self._items = factories.shop_factory.getItems(region, numItems, 
            quality)
        
        #Sort items
        sortItems(self._items)
    
    def enter(self, player):
        """
        Action sequence for shop.
        
        @param player:    The player object.
        """
        print ""
        print "- - - %s - - -" % self._name
        print "\"%s\"" % self._greetings

        #Determine and carry out player choice
        choice = None
        while choice != "quit":
            print \
"""
What is your choice?
\tCheck items             - 'check'
\tCheck item stats        - 'check stats'
\tSell item in inventory  - 'sell'
\tPurchase item           - 'purchase'
\tQuit                    - 'quit'
"""
            choice = raw_input("\"What do you want to do? \"")
            print ""
            
            if choice == "check":
                self.checkItems()
            elif choice == "check stats":
                self.checkItemsStats()
            elif choice == "sell":
                self.sellItems(player)
            elif choice == "purchase":
                self.buyItems(player)
            elif choice == "quit":
                self.leaveShop()
                break
            else:
                print "\"What?\""
                
            print ""
            raw_input("Press enter to continue. ")
            
    #Gives basic descriptions of items
    def checkItems(self):
        """
        Lists shop items in brief.
        """
        print "Here are our wares:"
        for item in self._items:
            print "\t%s: %s." % (item.getName(), item.getDescription())
            if isinstance(item, Weapon):
                print "\t\tAttack: %s" % item.getAttack()
            elif isinstance(item, Armor):
                print "\t\tDefense: %s" % item.getDefense()
            elif isinstance(item, Charm):
                if item.getAttack():
                    print "\t\tAttack: %s" % item.getAttack()
                if item.getDefense():
                    print "\t\tDefense: %s" % item.getDefense()
                if item.getHp():
                    print "\t\tHP Bonus: %s" % item.getHp()
            elif isinstance(item, Potion):
                print "\t\tHealing: %s" % item.getHealing()
            elif isinstance(item, Item):
                pass
            else:
                errorMsg = "Invalid item - shop_factory, checkItems()"
                raise AssertionError(errorMsg)
                
    #Gives advanced descriptions of items 
    def checkItemsStats(self):
        """
        Lists shop items in detail.
        """
        #Generate list of items without duplicates
        uniqueItems = []
        for item in self._items:
            if item not in uniqueItems:
                uniqueItems.append(item)
                
        #Print stats
        print "Item stats:"
        for item in uniqueItems:
            print "\t%s: %s." % (item.getName(), item.getDescription())
            if isinstance(item, Weapon):
                print "\t\t-Attack: %s" % item.getAttack()
                print "\t\t-Weight: %s" % item.getWeight()
                print "\t\t-Cost: %s" % item.getCost()
            elif isinstance(item, Armor):
                print "\t\t-Defense: %s" % item.getDefense()
                print "\t\t-Weight: %s" % item.getWeight()
                print "\t\t-Cost: %s" % item.getCost()
            elif isinstance(item, Charm):
                if item.getAttack():
                    print "\t\t-Attack: %s" % item.getAttack()
                if item.getDefense():
                    print "\t\t-Defense: %s" % item.getDefense()
                if item.getHp():
                    print "\t\t-HP Bonus: %s" % item.getHp()
                print "\t\t-Weight: %s" % item.getWeight()
                print "\t\t-Cost: %s" % item.getCost()
            elif isinstance(item, Potion):
                print "\t\t-Healing: %s" % item.getHealing()
                print "\t\t-Weight: %s" % item.getWeight()
                print "\t\t-Cost: %s" % item.getCost()
            elif isinstance(item, Item):
                print "\t\t-Weight: %s" % item.getWeight()
                print "\t\t-Cost: %s" % item.getCost()
            else:
                errorMsg = "Invalid item - shop_factory, checkItemsStats()"
                raise AssertionError(errorMsg)
                
    #For selling items in inventory to shop
    def sellItems(self, player):
        """
        Allows for player to sell items to shop. After each sale,
        the sold item gets added to shop wares.
        
        @param player:    The player object.
        """
        inventory = player.getInventory()
        itemValues = {}
        
        #User prompt
        print "Current inventory:"
        for item in player.getInventory():
            sellValue = constants.SELL_LOSS_PERCENTAGE * item.getCost()
            itemValues[item] = sellValue
            print "\t%s... with sell value: %s %s." % (item.getName(), 
            sellValue, constants.CURRENCY)
        itemToSell = raw_input("\nWhich item would you like to sell? ")
        
        #Find if item exists in inventory
        for item in inventory:
            if item.getName() == itemToSell:
                sellValue = itemValues[item]
                
                #Is user sure?
                choice = raw_input("Would you like to sell %s for %s %s?"
                " Response: yes/no. " % (item.getName(), sellValue, 
                constants.CURRENCY))
                
                #Sale execution - with affirmative
                if choice.lower() == "yes":
                    player.removeFromInventory(item)
                    player.increaseMoney(sellValue)
                    self._items.addItem(item)
                    print "Sold %s for %s." % (item.getName(), sellValue)
                    
                    #Check to see if item sold was theOneRing
                    result = self._checkTheOneRingSale(item)
                    #If it is, then theOneRing is removed from shop wares
                    if result:
                        print "\nSome strange men come by."
                        self._items.removeItem(item)
                
                #Player changes mind
                elif choice.lower() == "no":
                    print "Didn't sell item."
                
                #Invalid choice
                else:
                    print "Invalid choice."
                break
                    
    #Checks if sold item was theOneRing
    def _checkTheOneRingSale(self, item):
        """
        Helper method for item sales. 
        
        Checks to see if item sold was theOneRing.
        
        @param item:    The sold item.
        
        @return:        True if item is theOneRing; False otherwise.
        """
        if item is theOneRing:
            return True
        
        return False
        
    #For buying items from shop
    def buyItems(self, player):
        """
        Allows for items to buy items from shop wares. As player buys items,
        these items get removed from shop wares.
        
        @param player:     The player object.
        """
        #User prompt
        print "Items available for purchase:"
        for item in self._items:
            print "\t%s... with cost of %s." % (item.getName(), item.getCost())
        print ""
        print "%s has %s %s with which to spend." % (player.getName(), 
        player.getMoney(), constants.CURRENCY)
        print ""
        itemToPurchase = raw_input("Which item would you like to purchase? ")
        #Check to find object associated with user-given string
        for item in self._items:
            if itemToPurchase == item.getName():
                #Check to see if player has enough money to purchase item
                if player.getMoney() <= item.getCost():
                    print "Not enough money to purchase item."
                    return
                print ""
                #Actual purchase execution
                if not player.addToInventory(item):
                    return
                self._items.removeItem(item)
                player.decreaseMoney(item.getCost())
                print "%s puchased %s!" % (player.getName(), item.getName())
                break
        else:
            print "Can't purchase this item."

    #To leave shop
    def leaveShop(self):
        print "\"Have a good day.\""
        raw_input("Press enter to continue. ")