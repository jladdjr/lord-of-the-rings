#!/usr/bin/python

from cities.building import Building
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
import factories.shop_factory 
import constants

class Shop(Building):
    """
    Shops are buildings that allow player to buy and sell items.
    """
    def __init__(self, name, description, greetings, numItems, quality):
        """
        Initializes shop object.

        @param name:           The name of the shop.
        @param description:    A description of the shop.
        @param greetings:      The greetings the user gets as he enters a shop.
        @param numItems:       The number of items that can be bought at the shop.
        @param quality:        The quality of the items that may be bought at shop.
                               Ranges from 1-20.
        """
        Building.__init__(self, name, description, greetings)

        #Create items attributes and generate items objects
        self._numItems = numItems
        self._quality = quality
        self._items = factories.shop_factory.getItems(numItems, quality)
    
    def enter(self, player):
        """
        Returns the items in the shop.
        """
        print ""
        print "- - - %s - - -" % self._name
        print self._greetings

        #Determines and runs player choice
        CHECK_ITEMS = 1
        CHECK_ITEM_STATS = 2
        SELL_ITEM = 3
        PURCHASE_ITEM = 4
        QUIT = 5
        
        choice = None
        while choice != 5:
            print """
            What is your choice?
            1) Check items
            2) Check item stats
            3) Sell item in inventory
            4) Purchase item
            5) Quit
            """
            choice = int(raw_input("What do you want to do? "))
            if choice == CHECK_ITEMS:
                self.checkItems()
            elif choice == CHECK_ITEM_STATS:
                self.checkItemsStats()
            elif choice == SELL_ITEM:
                self.sellItems(player)
            elif choice == PURCHASE_ITEM:
                self.buyItems(player)
            elif choice == QUIT:
                self.leaveShop()
                break
            else:
                print "Huh?"

    #Gives basic descriptions of items
    def checkItems(self):
        print "Here are our wares:"
        for item in self._items:
            print "\t%s: %s." % (item.getName(), item.getDescription())
            if isinstance(item, Weapon):
                print "\t\tAttack: %s" % item.getAttack()
            elif isinstance(item, Armor):
                print "\t\tDefense: %s" % item.getDefense()
            else:
                print "\t\tHealing: %s" % item.getHealing()
                
    #Gives advanced descriptions of items 
    def checkItemsStats(self):           
        print "Item stats:"
        for item in self._items:
            print "\t%s: %s." % (item.getName(), item.getDescription())
            if isinstance(item, Weapon):
                print "\t\tAttack: %s" % item.getAttack()
                print "\t\tWeight: %s" % item.getWeight()
                print "\t\tCost: %s" % item.getCost()
            elif isinstance(item, Armor):
                print "\t\tDefense: %s" % item.getDefense()
                print "\t\tWeight: %s" % item.getWeight()
                print "\t\tCost: %s" % item.getCost()
            else:
                print "\t\tHealing: %s" % item.getHealing()
                print "\t\tWeight: %s" % item.getWeight()
                print "\t\tCost: %s" % item.getCost()

    #For selling items in inventory to shop
    def sellItems(self, player):
        #User prompt
        inventory = player.getInventory()
        sellableItems = []
        print "Current inventory:"
        for item in player.getInventory():
            if isinstance(item, Weapon) or isinstance(item, Armor):
                sellValue = constants.SELL_LOSS_PERCENTAGE * item.getCost()
                print "\t%s... with sell value: %s %s." % (item.getName(), sellValue, constants.CURRENCY)
                sellableItems.append(item)
        print ""

        itemToSell = raw_input("Which item would you like to sell? ")
        #Finds if item exists in inventory
        for item in sellableItems:
            if item.getName() == itemToSell:
                #Actual sale execution
                choice = raw_input("Would you like to sell %s for %s rubbles? Response: yes/no. " % (item.getName(), sellValue))
                if choice.lower() == "yes":
                    player.removeFromInventory(item)
                    player.increaseMoney(sellValue)
                    self._items.append(item)
                    print "Sold %s for %s." % (item.getName(), sellValue)
                elif choice.lower() == "no":
                    print "Didn't sell item." 
                else:
                    print "Invalid choice."
                    
    #For buying items from shop
    def buyItems(self, player):
        #User prompt
        print "Items available for purchase:"
        for item in self._items:
            print "\t%s... with cost of %s." % (item.getName(), item.getCost())
        print ""
        print "%s has %s rubles with which to spend." % (player.getName(), player.getMoney())
        itemToPurchase = raw_input("Which item would you like to purchase? ")
        #Check to find object associated with user-given string
        for item in self._items:
            if itemToPurchase == item.getName():
                #Check to see if player has enough money to purchase item
                if player.getMoney() <= item.getCost():
                    print "Not enough money to purchase item."
                    return
                #Actual purchase execution
                player.addToInventory(item)
                self._items.remove(item)
                player.decreaseMoney(item.getCost())
                print "%s puchased %s!" % (player.getName(), item.getName())
                break
        else:
            print "Can't purchase this item."

    #To leave shop
    def leaveShop(self):
        print "Leaving %s." % self._name
