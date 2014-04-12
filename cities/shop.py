#!/usr/bin/python

from cities.building import Building
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from factories.shop_factory import getItems
import constants

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
        @apram quality:        The quality of the items that may be bought at shop.
                               Ranges from 1-20.
        """
        Building.__init__(self, name, description, greetings)
        
        self._numItems = numItems
        self._quality = quality
        #TODO: Don't import function directly; instead, qualify it with shop_factory.getItems()
        self._items = getItems(numItems, quality)
    
    #TODO: Break this up using helper methods
    #TODO: Rename to enter() or enterBuilding()
    def execute(self, player):
        """
        Returns the items in the shop.
        """
        #TODO: Just use player
        self._player = player
        
        #TODO: Add space after %
        print ""
        print "- - - %s - - -" %self._name
        print self._greetings + "."

        #TODO: No magic numbers
        #Determine player choice
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
            choice = int(raw_input("Choice? "))

            #Gives basic descrptions of items
            if choice == 1:
                print "Here are our wares:"
                for item in self._items:
                    print "\t%s: %s." %(item.getName(), item.getDescription())
                    if isinstance(item, Weapon):
                        print "\t\tAttack: %s" %item.getAttack()
                    elif isinstance(item, Armor):
                        print "\t\tDefense: %s" %item.getDefense()
                    else:
                        print "\t\tHealing: %s" %item.getHealing()

            #Gives advanced descriptions of items            
            elif choice == 2:
                print "Item stats:"
                for item in self._items:
                    print "\t%s: %s." %(item.getName(), item.getDescription())
                    if isinstance(item, Weapon):
                        print "\t\tAttack: %s" %item.getAttack()
                        print "\t\tWeight: %s" %item.getWeight()
                        print "\t\tCost: %s" %item.getCost()
                    elif isinstance(item, Armor):
                        print "\t\tDefense: %s" %item.getDefense()
                        print "\t\tWeight: %s" %item.getWeight()
                        print "\t\tCost: %s" %item.getCost()
                    else:
                        print "\t\tHealing: %s" %item.getHealing()
                        print "\t\tWeight: %s" %item.getWeight()
                        print "\t\tCost: %s" %item.getCost()
                    
            #For selling items in inventory to shop
            elif choice == 3:
                inventory = self._player.getInventory()
                
                print "Current inventory:"
                for item in self._player.getInventory():
                    print "\t%s... with sell value: %s." %(item.getName(), constants.SELL_LOSS * item.getCost())
                print ""

                itemToSell = raw_input("Which item would you like to sell? ")
                for item in inventory:
                    if item.getName() == itemToSell:
                        sellValue = constants.SELL_LOSS * item.getCost()
                        choice = raw_input("Would you like to sell %s for %s rubles? Response: y/n. " %(item.getName(), sellValue))
                        if choice.lower() == "y":
                            player.removeFromInventory(item)
                            player.increaseMoney(sellValue)
                            self._items.append(item)
                            print "Sold %s for %s." %(item.getName(), sellValue)
                        elif choice.lower() == "n":
                            print "Didn't sell item." 
                        else:
                            print "Invalid choice."

            #For buying items from shop
            elif choice == 4:
                #User prompt
                print "Items available for purchase:"
                for item in self._items:
                    print "\t%s... with cost of %s." %(item.getName(), item.getCost())
                print ""
                #TODO: Use currency name from constanst.py instead
                print "%s has %s rubles with which to spend." %(player.getName(), player.getMoney())
                itemToPurchase = raw_input("Which item would you like to purchase? ")
                #Check to find object associated with user-given string

                #TODO: Consider replacing this code with containsItemWithName() (after Dmitriy pushes code for the method)
                for item in self._items:
                    if itemToPurchase == item.getName():
                        #Check to see if player has enough money to purchase item
                        if self._player.getMoney() <= item.getCost():
                            print "Not enough money to purchase item."
                            return
                        #Actual purchase execution
                        else:
                            player.addToInventory(item)
                            self._items.remove(item)
                            player.decreaseMoney(item.getCost())
                            print "%s puchased %s!" %(self._player.getName(), item.getName())
                            break
                else:
                    print "Can't purchase this item."

            #To leave shop      
            elif choice == 5:
                print "Leaving %s." %self._name

            #For invalid choices
            else:
                print "Invalid choice."
