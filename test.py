#!/usr/bin/python

import unittest
import signal

import xmlrunner
from mock import (MagicMock, patch)

class GameTest(unittest.TestCase):
    """
    Tests Game class.
    """
    def testNextTurn(self):
        from game import Game
        g = Game()

        #Create mock objects
        helpCommand = MagicMock()
        helpCommand.execute = MagicMock()
        g._parser.getNextCommand = MagicMock(return_value=helpCommand)

        g._nextTurn()
        self.assertTrue(helpCommand.execute.called, "Game._nextTurn() failed to execute command")

class ParserTest(unittest.TestCase):
    """
    Tests Parser class.
    """
    def testGetNextCommand(self):
        from parser import Parser
        commandWords = MagicMock()
        p = Parser(commandWords)

        #Create mock objects
        #raw_input = MagicMock(side_effect=["unrecognized command", "good command"])
        p._commandRecognized = MagicMock(side_effect=[False, True])
        fakeCommand = MagicMock()
        p._commandWords.getCommand = MagicMock(return_value=fakeCommand) 

        #Patch raw_input and call getNextCommand()
        rawInputMock = MagicMock(side_effect=["unrecognized cmd", "valid cmd"])
        with patch('parser.raw_input', create=True, new=rawInputMock):
            command = p.getNextCommand()

        #Assert calls made
        errorMsg = "Expected raw_input to be called twice."
        self.assertEqual(rawInputMock.call_count, 2, errorMsg)
        errorMsg = "Expected Parser._commandRecognized() to be called twice."
        self.assertEqual(p._commandRecognized.call_count, 2, errorMsg)
        errorMsg = "Parser.getNextCommand() did not respond expected command."
        self.assertEqual(command, fakeCommand, errorMsg)

    def testCommandRecognized(self):
        from parser import Parser
        commandWords = MagicMock()
        commandWords.isCommand = MagicMock(return_value=True)
        p = Parser(commandWords)

        result = p._commandRecognized("valid command")

        errorMsg = "Expected Parser._commandRecognized() to return True."
        self.assertTrue(result, errorMsg) 

class ItemTest(unittest.TestCase):
    """
    Tests Item class.
    """
    def testItem(self):
        from items.item import Item
        
        name = "Generic item"
        description = "Generic description"
        weight = 9

        item = Item(name, description, weight)

        errorMsg = "Expected item name to be '%s'." % name
        self.assertEqual(item.getName(), name, errorMsg)
        errorMsg = "Expected item description to be '%s'." % description 
        self.assertEqual(item.getDescription(), description, errorMsg)
        errorMsg = "Expected item weight to be '%s'." % weight 
        self.assertEqual(item.getWeight(), weight, errorMsg)

class ItemSetTest(unittest.TestCase):
    """
    Tests ItemSet class.
    """
    INITIAL_COUNT = 3
    INITIAL_WEIGHT = 4

    def setUp(self):
        from items.item import Item
        from items.item_set import ItemSet

        sword = Item("sword", "made by elves", 2)
        helmet = Item("helmet", "made by men", 1)
        potion = Item("potion", "restores health", 1)

        self._itemList = [sword, helmet, potion]
        self._items = ItemSet([sword, helmet, potion])

    def tearDown(self):
        self._itemList = self._items = None

    def testInitItemSet(self):
        errorMsg = "ItemSet object has more objects than it was given " \
                    "during initialization."
        self.assertEqual(len(self._items._items), ItemSetTest.INITIAL_COUNT, errorMsg)

        errorMsg = "ItemSet object does not include all objects given " \
                    "during initialization."
        for item in self._itemList:
            self.assertTrue(item in self._items._items, errorMsg)

    def testCountItems(self):
        expectedCount = ItemSetTest.INITIAL_COUNT
        actualCount = self._items.count()
        
        errorMsg = "Actual count and expected count different for ItemSet object."
        self.assertEqual(expectedCount, actualCount, errorMsg)

    def testAddRemoveContainsItems(self):
        from items.item import Item
        antidote = Item("antidote", "cures poison", 1)

        #Verify item not included in collection
        errorMsg = "ItemSet.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

        #Add item
        self._items.addItem(antidote)

        errorMsg = "ItemSet.containsItem() failed to identify existing item." 
        self.assertTrue(self._items.containsItem(antidote), errorMsg)

        errorMsg = "ItemSet.containsItemWithName() failed to identify existing item."
        self.assertTrue(self._items.containsItemWithName("antidote"), errorMsg)

        #Remove item
        self._items.removeItem(antidote)

        errorMsg = "ItemSet.containsItem() claimed to contain item not present."
        self.assertFalse(self._items.containsItem(antidote), errorMsg)

    def testItemsWeight(self):
        from items.item import Item 

        errorMsg = "Initial weight of ItemSet object incorrect."
        expectedWeight = ItemSetTest.INITIAL_WEIGHT
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        heavyRock = Item("heavy rock", "weighs a ton", 2000)

        #Add item
        self._items.addItem(heavyRock)

        errorMsg = "ItemSet.weight() reported incorrect weight." 
        expectedWeight += 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

        #Remove item
        self._items.removeItem(heavyRock)

        expectedWeight -= 2000
        actualWeight = self._items.weight()
        self.assertEqual(expectedWeight, actualWeight, errorMsg)

    def testItemSetIter(self):
        #Verify iterator returns by ItemSet object visits the exact
        #collection of objects added to ItemSet

        #(Implicitly) use iterator in for loop
        for item in self._items:
            #Verify item returned is recognized
            errorMsg = "ItemSet iterator returned unrecognized object."
            self.assertTrue(item in self._itemList, errorMsg)

            #Remove item from original list of items
            self._itemList.remove(item)

        #Assert all items are accounted for
        errorMsg = "ItemSet object contained Item not added during initialization."
        self.assertEqual(len(self._itemList), 0, errorMsg)

class SpaceTest(unittest.TestCase):
    """
    Test for spaces.
    """
    def testItems(self):
        from space import Space
        from items.item import Item

        #Prepare items
        blade = Item("blade", "appears to be dull", 1)
        bow = Item("bow", "long bow", 2) 

        #Create space
        space = Space("shire", "Home of the Hobbits.", "Mordor")
        items = space.getItems()

        #Assert space initially empty
        errorMsg = "New space contains items; should be empty" 
        self.assertEqual(items.count(), 0, errorMsg)

        errorMsg = "Space claims to contain item even though it is empty."
        self.assertFalse(space.containsItem(blade), errorMsg)
        self.assertFalse(space.containsItem(bow), errorMsg)

        #Add blade
        space.addItem(blade)
        errorMsg = "Space failed to report that it contained item known to exist."
        self.assertTrue(space.containsItem(blade), errorMsg)

        #Add bow 
        space.addItem(bow)
        self.assertTrue(space.containsItem(bow), errorMsg)

        #Get room's items. Assert blade and bow exist
        items = space.getItems()
        self.assertEqual(items.count(), 2, "Room should contain exactly two items.")
        self.assertTrue(items.containsItem(blade), "Could not find blade in room's set of items.")
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")

        #Remove blade
        space.removeItem(blade)
        errorMsg = "Space claims to have item that was removed."
        self.assertFalse(space.containsItem(blade), errorMsg)
        errorMsg = "Space missing item that should still exist."
        self.assertTrue(space.containsItem(bow), errorMsg)

        #Get room's items. Assert only bow exists
        items = space.getItems()
        self.assertEqual(items.count(), 1, "Room should contain exactly one item.")
        self.assertFalse(items.containsItem(blade), 
                "Blade found in room (even though it was removed).")
        self.assertFalse(items.containsItemWithName("blade"), "Blade found in room (even though it was removed).")
        self.assertTrue(items.containsItem(bow), "Could not find bow in room's set of items.")

    def testRegion(self):
        from space import Space
        import constants

        space = Space("West Emnet", "Horses for riding", "Rohan")

        errorMsg = "Space regionType test failed."
        self.assertEquals(space.getRegion(), "Rohan", errorMsg)

    def testCities(self):
        from space import Space
        from cities.city import City

        #Create city
        newYorkCity = City("City", "An enormous city", "Come test here")

        #Create space
        newYork = Space("Space", "A huge space", "Welcome to our space", city = newYorkCity)

        #Assert city in space
        errorMsg = "Space should contain city but does not."
        self.assertEqual(newYork.getCity(), newYorkCity, errorMsg)

    def testUniquePlace(self):
        from space import Space
        from unique_place import UniquePlace

        #Create UniquePlace
        dmitriyHouse = UniquePlace("Dmitriy's House", "Lots of vodka", "[knocks once]")

        #Create space
        chocolateMountain = Space("Chocolate Mountain", "Chocolate rain here", "Welcome", uniquePlace = dmitriyHouse)
        
        #Assert uniquePlace in space
        errorMsg = "Space should contain uniquePlace but does not."
        self.assertEqual(chocolateMountain.getUniquePlace(), dmitriyHouse, errorMsg)
        
class MovementTest(unittest.TestCase):
    """
    Tests movement methods of space and movement commands.  
    """
    def testMovement(self):
        """
        General, encompassing test for movement, including movement commands.
        """
        from space import Space
        from player import Player
        from commands.north_command import NorthCommand
        from commands.south_command import SouthCommand
        from commands.west_command import WestCommand
        from commands.east_command import EastCommand
        from constants import Direction
        
        space = Space("Shire", "Home of the hobbits", "Mordor")
        player = Player("Russian", space)
        
        northCmd = NorthCommand("North", "Moves player north", player)
        southCmd = SouthCommand("South", "Moves player south", player)
        eastCmd = EastCommand("East", "Moves player east", player)
        westCmd = WestCommand("West", "Moves player west", player)
        
        #Non-movement case - ports not created
        errorMsg = "Player should still be in space but is not."

        northCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        southCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        eastCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        westCmd.execute()
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = Space

        #Create destinations and two-way ports
        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")

        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test getExit method for destination spaces
        errorMsg = "getExit() test failed."
        self.assertEqual(north.getExit("south"), space, errorMsg)
        self.assertEqual(south.getExit("north"), space, errorMsg)
        self.assertEqual(east.getExit("west"), space, errorMsg)
        self.assertEqual(west.getExit("east"), space, errorMsg)

        #Test ports created using _isExit() for space
        errorMsg = "Ports are supposed to be created but are not - tested using _isExit()."
        self.assertEqual(space._isExit("north"), True, errorMsg)
        self.assertEqual(space._isExit("south"), True, errorMsg)
        self.assertEqual(space._isExit("east"), True, errorMsg)
        self.assertEqual(space._isExit("west"), True, errorMsg)

        #Test ports created without using direct access for Space
        errorMsg = "Ports are supposed to be created but are not - by direct attribute access."
        self.assertEqual(space._exits[Direction.NORTH], north, errorMsg)
        self.assertEqual(space._exits[Direction.SOUTH], south, errorMsg)
        self.assertEqual(space._exits[Direction.EAST], east, errorMsg)
        self.assertEqual(space._exits[Direction.WEST], west, errorMsg)

        #Test ports created without using direct access for destination Spaces
        errorMsg = "Two-way ports were supposed to have been created but were not - by direct attribute access."
        self.assertEqual(north._exits[Direction.SOUTH], space, errorMsg)
        self.assertEqual(south._exits[Direction.NORTH], space, errorMsg)
        self.assertEqual(east._exits[Direction.WEST], space, errorMsg)
        self.assertEqual(west._exits[Direction.EAST], space, errorMsg)
                                      
        #Test two-way movement
        northCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        southCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)
        player._location = space

        southCmd.execute()
        errorMsg = "Player should be in south space but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        player._location = space
        northCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)
        
        eastCmd.execute()
        errorMsg = "Player should be in east space but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        player._location = space
        westCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)
        
        westCmd.execute()
        errorMsg = "Player should be in west space but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)
        player._location = space
        eastCmd.execute()
        errorMsg = "Player should be in space but is not."
        self.assertEqual(player.getLocation(), space, errorMsg)

        #Test clearExit() method
        errorMsg = "Port should have been cleared but was not."

        space.clearExit("north")
        self.assertTrue(space._exits[Direction.North], None, errorMsg)
                        
        space.clearExit("south")
        self.assertTrue(space._exits[Direction.South], None, errorMsg)
        
        space.clearExit("east")
        self.assertTrue(space._exits[Direction.East], None, errorMsg)
        
        space.clearExit("west")
        self.assertTrue(space._exits[Direction.West], None, errorMsg)

        #Test _isExit() method - where there are no ports
        errorMsg = "_isExit() failed to return the correct port - no ports exit."
        self.assertTrue(space._isExit("north"), None, errorMsg)
        self.assertTrue(space._isExit("south"), None, errorMsg)
        self.assertTrue(space._isExit("east"), None, errorMsg)
        self.assertTrue(space._isExit("west"), None, errorMsg)

    def testMovement2(self):
        """
        Smaller test for one-way ports and one-way movement.
        """
        from space import Space
        from player import Player
        from commands.north_command import NorthCommand
        from commands.south_command import SouthCommand
        from commands.west_command import WestCommand
        from commands.east_command import EastCommand
        
        space = Space("Shire", "Home of the hobbits", "Mordor")
        player = Player("Russian", space)
        
        northCmd = NorthCommand("North", "Moves player north", player)
        southCmd = SouthCommand("South", "Moves player south", player)
        eastCmd = EastCommand("East", "Moves player east", player)
        westCmd = WestCommand("West", "Moves player west", player)
        
        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")
        
        #Create one-way ports
        space.createExit("north", north, outgoingOnly = True)
        space.createExit("south", south, outgoingOnly = True)
        space.createExit("east", east, outgoingOnly = True)
        space.createExit("west", west, outgoingOnly = True)

        #Test one-way movement
        northCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        southCmd.execute()
        errorMsg = "Player should be in north space but is not."
        self.assertEqual(player.getLocation(), north, errorMsg)
        
        player._location = space
        southCmd.execute()
        errorMsg = "Player should be in south space but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        northCmd.execute()
        errorMsg = "Player should be in south but is not."
        self.assertEqual(player.getLocation(), south, errorMsg)
        
        player._location = space
        eastCmd.execute()
        errorMsg = "Player should be in east space but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        westCmd.execute()
        errorMsg = "Player should be in east but is not."
        self.assertEqual(player.getLocation(), east, errorMsg)
        
        player._location = space
        westCmd.execute()
        errorMsg = "Player should be in west space but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)
        eastCmd.execute()
        errorMsg = "Player should be in west but is not."
        self.assertEqual(player.getLocation(), west, errorMsg)

class PickUpTest(unittest.TestCase):
    """
    Test PickUp class.
    """
    def testExecute(self):
        from space import Space
        from player import Player
        from items.item import Item
        from commands.pick_up_command import PickUpCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        item = Item("Dagger", "A trusty blade", 2)
        pickUpCmd = PickUpCommand("pick up", "Picks up an object", player)
        
        space.addItem(item)

        #Assert item in space but not in inventory and equipment
        self.assertTrue(space.containsItem(item), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(item), "Player should not have item but does in inventory.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item but does in equipment.")
            
        #Execute pickUpCmd and assert item in player inventory but not in space and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.pick_up_command.raw_input', create=True, new=rawInputMock):
            pickUpCmd.execute()
            
        self.assertFalse(space.containsItem(item), "Space should not have item but does.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player should not have item in equipment.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(item), "Player should have item in inventory but does not.")
        
class DropTest(unittest.TestCase):
    """
    Test Drop class.
    """
    def testExecute(self):
        """
        Test case where item in inventory and equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)

        player.addToInventory(weapon)
        player.equip(weapon)

        #Asserts item in player inventory and equipped but not in space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

        equipped = player.getEquipped()
        self.assertTrue(equipped.containsItem(weapon), "Equipped should have item but does not.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have item but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have item but does.")

    def testExecute2(self):
        """
        Test for case: item in inventory and but not in equipment.
        """
        from space import Space
        from player import Player
        from items.weapon import Weapon
        from commands.drop_command import DropCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        dropCmd = DropCommand("drop", "Drops an object from inventory to space", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)

        player.addToInventory(weapon)
        
        #Asserts item in player inventory but not in equipped and space
        self.assertFalse(space.containsItem(weapon), "Space should not have item but does.")
        
        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have item but does not.")

        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipped should not have item but does.")

        #Assert item in space but not in player inventory and not in equipment
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.drop_command.raw_input', create=True, new=rawInputMock):
            dropCmd.execute()
            
        self.assertTrue(space.containsItemString("Dagger"), "Space should have item but does not.")
        
        inventory = player.getInventory()
        self.assertFalse(inventory.containsItem(weapon), "Inventory should not have item but does.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Equipment should not have item but does.")
        
class DescribeTest(unittest.TestCase):
    """
    Tests Describe class.
    """
    def testExecute(self):
        from player import Player
        from space import Space
        from commands.describe_command import DescribeCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        descCmd = DescribeCommand("describe", "Gives description of space", player)

        descCmd.execute()
        
        #Tests that execute returns space description
        #TODO: find a way to make sure that a print statement came out correctly.
        """
        self.assertEqual(descCmd.execute(), "Home of the Hobbits", \
            "Describe command gave incorrect description.")
        """

class EquipTest(unittest.TestCase):
    """
    Tests Equip Command.
    """
    def equippingItemsNotInInventory(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.equip_command import EquipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)
        
        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of Faith", 2, 2, 2)

        #Trying to equip items not in inventory
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Player equipped item not in inventory.")
        self.assertFalse(equipped.containsItem(armor), "Player equipped item not in inventory.")

    def equippingUnequippableItems(self):
        from player import Player
        from space import Space
        from items.item import Item
        from commands.equip_command import EquipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)
        
        item = Item("Charm", "Unknown effects", 1)
        
        inventory = player.getInventory()
        inventory.addItem(item)

        #Trying to equip item that cannot be equipped (e.g. item is not instance of Armor or Weapon)
        rawInputMock = MagicMock(return_value="Charm")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(item), "Player equipped item of Item class.")

    def equippingEquippableItems(self):
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2) 

        inventory = player.getInventory()
        inventory.addItem(weapon)
        inventory.addItem(armor)

        #Equipping equippable items
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()
            
        equipped = player.getEquipped()
        
        self.assertTrue(equipped.containsItem(weapon), "Player failed to equip equipable item.")
        self.assertTrue(equipped.containsItem(armor), "Player failed to equip equipable item.")

    def equippingAlreadyEquippedItem(self):
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        inventory = player.getInventory()
        inventory.addItem(weapon)
        inventory.addItem(armor)
        
        equipped = player.getEquipped()
        equipped.addItem(weapon)
        equipped.addItem(armor)

        #Test - preconditions
        errorMsg = "Weapon is supposed to be in player._equipped but is not."
        self.assertTrue(weapon in player._equipped, errorMsg)
        errorMsg = "Armor is supposed to be in player._equipped but it is not."
        self.assertTrue(armor in player._equipped, errorMsg)
        errorMsg = "player._equipped is supposed to have two items but does not."
        self.assertEqual(player._equipped.count(), 2, errorMsg)

        #Equipping an item that is already equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 
            
        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        #Test still only two equipped items
        errorMsg = "Weapon is supposed to be in player._equipped but is not."
        self.assertTrue(weapon in player._equipped, errorMsg)
        errorMsg = "Armor is supposed to be in player._equipped but it is not."
        self.assertTrue(armor in player._equipped, errorMsg)
        self.assertEqual(equipped.count(), 2, "Player is supposed to have two equipped items but lists more.")

    def playerStatsUpdateWeapon(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)

        #Create default
        defaultAttack = player._attack

        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute() 

        errorMsg = "Weapon should be equipped but is not."
        self.assertTrue(player._equipped.contains(weapon), errorMsg)

        #Test for change
        errorMsg = "Player._attack changed with weapon equip when it should not have."
        self.assertEqual(player._attack, defaultAttack, errorMsg)
        errorMsg = "player._weaponAttack not updated to correct value."
        self.assertEqual(player._weaponAttack, weapon._attack, errorMsg)
        errorMsg = "Player._totalAttack not updated to correct value."
        self.assertEqual(player._totalAttack, defaultAttack + weapon._attack, errorMsg)

    def playerStatsUpdateArmor(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.equip_command import EquipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        equipCmd = EquipCommand("Equip", "Equips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)

        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.equip_command.raw_input', create=True, new=rawInputMock):
            equipCmd.execute()

        errorMsg = "Armor should be equipped but is not."
        self.assertTrue(player._equipped.contains(armor), errorMsg)
        
        #Test for change
        errorMsg = "player._armorDefense stat was not updated correctly."
        self.assertEqual(player._armorDefense, armor._defense, errorMsg)
                         
class UnequipTest(unittest.TestCase):
    """
    Tests Unequip Command.
    """
    def unequipWhenItemNotCurrentlyEquipped(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "of faith", 2, 2, 2)

        #Attempting to unequip item not currently equipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        #TODO: find way to make sure that 30-32 in unequip is called
        errorMsg = "Player should not have weapon in equipped but does."
        self.assertFalse(player._equipped.contains(weapon), errorMsg)
        errorMsg = "Player should not have armor in equipped but does."
        self.assertFalse(player._equipped.contains(armor), errorMsg)            

    def unequippingUnequippableItem(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("unequip", "Unequips currently equipped item", player)

        weapon = Weapon("Dagger", "A trusty blade", 2, 2, 2)
        armor = Armor("Shield", "Round", 1, 1, 1)

        player.equip(weapon)
        player.equip(armor)

        errorMsg = "Weapon should be in player._equipped but is not."
        self._assertTrue(player._equipped.contains(weapon), errorMsg)
        errorMsg = "Armor should be in player._equipped but is not."
        self._assertTrue(player._equipped.contains(armor), errorMsg)

        #Attempting to unequip item that may be unequipped
        rawInputMock = MagicMock(return_value="Dagger")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        rawInputMock = MagicMock(return_value="Shield")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute()

        inventory = player.getInventory()
        self.assertTrue(inventory.containsItem(weapon), "Inventory should have weapon and does not.")
        self.assertTrue(inventory.containsItem(armor), "Inventory should have armor and does not.")
        
        equipped = player.getEquipped()
        self.assertFalse(equipped.containsItem(weapon), "Failed to unequip item that it should have.")
        self.assertFalse(equipped.containsItem(armor), "Failed to unequip item that it should have.")

    def playerWeaponStatsUpdate(self):
        from player import Player
        from space import Space
        from items.weapon import Weapon
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)
        player.equip(weapon)
        
        rawInputMock = MagicMock(return_value="Sword of the Spirit")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        #Test for change back to player defaults
        errorMsg = "player._weaponAttack should be zero but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "player._totalAttack should be attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def playerArmorStatsUpdate(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        from commands.unequip_command import UnequipCommand
        import constants
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        unequipCmd = UnequipCommand("Unequip", "Unequips item in inventory to player", player)

        armor = Armor("Shield of Faith", "For quenching fiery darts", 1, 1, 1)
        player.equip(armor)
        
        rawInputMock = MagicMock(return_value="Shield of Faith")
        with patch('commands.unequip_command.raw_input', create=True, new=rawInputMock):
            unequipCmd.execute() 

        #Test for change back to player defaults
        errorMsg = "player._armorDefense should be zero after unequip but is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)

class UsePotionTest(unittest.TestCase):
    """
    Tests UsePotion command.
    """
    def testExecute(self):
        from commands.use_potion_command import UsePotionCommand
        from space import Space
        from player import Player
        from items.potion import Potion

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        inventory = player.getInventory()
        usePotionCmd = UsePotionCommand("use potion", "Uses potion in inventory.", player)
        
        player._maxHp = 20
        player._hp = 1
        healing = 9
        correctFinalHp = player._hp + healing
        
        potion = Potion("Enormous Potion", "So big", 1, healing, 10)
        player._inventory.addItem(potion)
        
        rawInputMock = MagicMock(return_value="Enormous Potion")
        with patch('commands.use_potion_command.raw_input', create = True, new = rawInputMock):
            usePotionCmd.execute()
            
        errorMsg = "Inventory still contains potion when it should not."
        self.assertFalse(inventory.containsItem(potion), errorMsg)
        errorMsg = "Player health not at correct amount."
        self.assertEqual(player._hp, correctFinalHp, errorMsg)
            
class WeaponTest(unittest.TestCase):
    """
    Tests Weapon class.
    """
    def testInit(self):
        from items.weapon import Weapon

        sword = Weapon("Sword", "A cheap sword", 3, 2, 1)

        #Tests for correct initialization
        self.assertEqual(sword.getName(), "Sword", "Name did not initialize correctly.")
        self.assertEqual(sword.getDescription(), "A cheap sword", "Description did not initialize correctly.")
        self.assertEqual(sword.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(sword.getAttack(), 2, "Damage did not initialize correctly.")
        self.assertEqual(sword.getCost(), 1, "Cost did not initialize correctly.")

class ArmorTest(unittest.TestCase):
    """
    Tests Armor class.
    """
    def testInit(self):
        from items.armor import Armor
        
        shield = Armor("Shield", "A cheap shield", 3, 2, 1)

        #Tests that shield initialized correctly
        self.assertEqual(shield.getName(), "Shield", "Name did not initialize correctly.")
        self.assertEqual(shield.getDescription(), "A cheap shield", "Description did not initialize correctly.")
        self.assertEqual(shield.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(shield.getDefense(), 2, "Defense did not initialize correctly.")
        self.assertEqual(shield.getCost(), 1, "Cost did not initialize correctly.")

class Potion(unittest.TestCase):
    """
    Tests Potion class.
    """
    def testInit(self):
        from items.potion import Potion

        potion = Potion("Potion", "A small potion", 3, 2, 1)
        
        #Tests for correct initialization
        self.assertEqual(potion.getName(), "Potion", "Name did not initialize correctly.")
        self.assertEqual(potion.getDescription(), "A small potion", "Description did not initialize correctly.")
        self.assertEqual(potion.getWeight(), 3, "Weight did not initialize correctly.")
        self.assertEqual(potion.getHealing(), 2, "Healing did not initialize correctly.")
        self.assertEqual(potion.getCost(), 1, "Cost did not initialize correctly.")

class PlayerTest(unittest.TestCase):
    """
    Tests Player class.
    """
    def testInit(self):
        from player import Player
        from space import Space
        from items.item_set import ItemSet
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        #Test for correct initialization
        self.assertEqual(player._name, "Frodo", "Player name did not initialize correctly.")
        self.assertEqual(player._location, space, "Player location did not initialize correctly.")
        self.assertEqual(player._money, constants.STARTING_MONEY, "Money did not initialize correctly.")
        
        emptyList = []
        self.assertEqual(player._inventory.getItems(), emptyList, "Player inventory was not initialized correctly.")
        self.assertEqual(player._equipped.getItems(), emptyList, "Player equipped was not initialized correctly.")
        
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, "Player experience was not initialized.")
        self.assertEqual(player._level, constants.STARTING_LEVEL, "Player level was not initialized.")
        
        self.assertEqual(player._maxHp, constants.HP_STAT, "Player max Hp was not initialized.")
        self.assertEqual(player._hp, constants.HP_STAT, "Player Hp was not initialized.")
        self.assertEqual(player._attack, constants.ATTACK_STAT, "Player attack was not initialized.")

        self.assertEqual(player._weaponAttack, constants.STARTING_WEAPON_ATTACK, "Player attack bonus was not initialized.")
        self.assertEqual(player._armorDefense, constants.STARTING_ARMOR_DEFENSE, "Player defense bonus was not initialized.")
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, "Player ._totalAttack did not initiate correctly.")
        
    def testAttack(self):
        from player import Player
        from space import Space
        from monsters.monster import Monster
        #TODO: use mock objects to rewrite this test
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        stats = [10, 1, 1]
        monster = Monster("Orc", "An orc.", stats, "Moof", "Meep")
        
        #Check monster health default stats
        self.assertEqual(monster._hp, 10, "Monster Hp did not initialize correctly.")
        
        #Player attacks monster
        player.attack(monster)
    
        expectedHp = 10 - (player._totalAttack)
        
        self.assertEqual(monster._hp, expectedHp, "Monster attack failed to work correctly.")

    def testTakeDamage(self):
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        
        #When attack is more than maxHp
        OVERKILL = player._maxHp + 10000

        player.takeAttack(OVERKILL)
        errorMsg = "Overkill testcase in testTakeDamage() failed."
        self.assertEqual(player._hp, 0, errorMsg)

        player._hp = player._maxHp
        
        #When attack is less than maxHp
        UNDERKILL = player._maxHp - 1

        player.takeAttack(UNDERKILL)
        errorMsg = "Underkill test case in testTakeDamage() failed."
        self.assertEqual(player._hp, 1, errorMsg)

    def takeDamageArmor(self):
        from player import Player
        from space import Space
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 2, 2, 2)
        player.equip(armor)

        #Testcase - armorDefense is more than attack
        player._hp = 10
        player.takeAttack(1)
        errorMsg = "Testcase - armorDefense is more than attack failed. %s" %player._hp
        self.assertEqual(player._hp, 10, errorMsg)
        
        #Testcase - armorDefense is attack
        player._hp = 10
        player.takeAttack(2)
        errorMsg = "Testcase - armorDefense is attack failed."
        self.assertEqual(player._hp, 10, errorMsg)
        
        #Testcase - armorDefense is less than attack
        player._hp = 10
        player.takeAttack(3)
        errorMsg = "Testcase - armorDefense is less than attack failed."
        self.assertEqual(player._hp, 9, errorMsg)
        
    def testIncreaseExperience(self):
        from player import Player
        from space import Space
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        #Test starting experience
        errorMsg = "Player starting experienced failed to initialize correctly."
        self.assertEqual(player._experience, constants.STARTING_EXPERIENCE, errorMsg)

        #Test increaseExperience()
        player.increaseExperience(10000)
        
        errorMsg = "Player experience failed to increase."
        self.assertTrue(player._experience > constants.STARTING_EXPERIENCE, errorMsg)
        
    def _updateLevel(self):
        from player import Player
        from space import Space
        from math import floor
        import constants

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        #Determine default player stats
        defaultLevel = self._level
        defaultMaxHp = self._maxHp
        defaultAttack = self._attack
        defaultTotalAttack = self._totalAttack

        #Increase player experience and run _updateLevel
        originalExperience = player._experience
        newExperience = 1000
        player._experience = newExperience + originalExperience
        player._updateLevel()

        #Test that stats have increased
        self.assertTrue(player._level > defaultLevel, "Player level did not increase.")
        self.assertTrue(player._maxHp > defaultMaxHp, "Player Hp did not increase.")
        self.assertTrue(player._attack > defaultAttack, "Player attack did not increase.")
        self.assertTrue(player._totalAttack > defaultTotalAttack, "Player totalAttack did not increase.")
        
        #Test for proper player stat change
        self.assertEqual(player._level, floor(player._experience/20) + 1, "Player level is incorrect.")
        self.assertEqual(player._maxHp, player._level * constants.HP_STAT, "Player Hp is incorrect.")
        self.assertEqual(player._attack, player._level * constants.ATTACK_STAT, "Player attack is incorrect.")
        self.assertEqual(player._totalAttack, player._attack + player._weaponAttack, "Player totalAttack is incorrect.")
        
    def testHeal(self):
        #Heal where healing amount is greater than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        attackAmount = 2
        healAmount = 3
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, player._maxHp, "Healing testcase #1 failed.")

        #Heal where healing amount is less than total amount possible
        from player import Player
        from space import Space

        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        attackAmount = 3
        healAmount = 2
        difference = attackAmount - healAmount
        
        player.takeAttack(attackAmount)
        player.heal(healAmount)

        self.assertEqual(player._hp, player._maxHp - difference, "Healing testcase #2 failed.")
        
    def testEquipUnequip(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)
        
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)

        #Pretest player-specific items-based attributes
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "_totalAttack should be simply attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

        #Attempt to equip new items
        player.equip(newItem)
        self.assertFalse(newItem in player.getEquipped(), "Equipped %s and should not have." % newItem)
        player.equip(newWeapon)
        self.assertTrue(newWeapon in player.getEquipped(), "Failed to equip %s" % newWeapon)
        player.equip(newArmor)
        self.assertTrue(newArmor in player.getEquipped(), "Failed to equip %s" % newArmor)

        #Post-test player-specific items-based attributes
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, newWeapon.getAttack(), errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, newArmor.getDefense(), errorMsg)
        errorMsg = "_totalAttack should have been updated but was not."
        self.assertEqual(player._totalAttack, player._attack + newWeapon.getAttack(), errorMsg)
        
        #Attempt to unequip items
        player.unequip(newWeapon)
        self.assertFalse(newWeapon in player.getEquipped(), "Failed to unequip %s" % newWeapon)
        player.unequip(newArmor)
        self.assertFalse(newArmor in player.getEquipped(), "Failed to unequip %s" % newArmor)

        #Check to see that item-specific attributes are reset to pre-equip figures
        errorMsg = "_weaponAttack should be 0 but it is not - unequip."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "armorDefense should be 0 but it is not - unequip."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "totalAttack should be simply attack but it is not - unequip."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)
        
    def addToInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        #Test add items to inventory
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        errorMsg = "Failed to add in legimiate item to inventory"
        self.assertTrue(newItem in player._inventory, errorMsg)
        self.assertTrue(newWeapon in player._inventory, errorMsg)
        self.assertTrue(newArmor in player._inventory, errorMsg)
        
        #Test to add items already in inventory to inventory
        numberOfItems = len(player._inventory)
        
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        
        newNumberOfItems = len(player._inventory)
        errorMsg = "Number of items increased when it should not have."
        self.assertEqual(numberOfItems, newNumberOfItems, errorMsg)

    def removeFromInventory(self):
        from player import Player
        from space import Space
        from items.item import Item
        from items.weapon import Weapon
        from items.armor import Armor
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        newItem = Item("Chainik Reakettle", "Makes good tea", 1)
        newWeapon = Weapon("Gun of Hurlocker", "Oppressive, but friendly", 2, 3, 1)
        newArmor = Armor("Cookies of Miles", "Defends against sadness", 2, 4, 1)

        #Test correct character initialization
        player.addToInventory(newItem)
        player.addToInventory(newWeapon)
        player.addToInventory(newArmor)
        errorMsg = "Failed to initialize test character correctly."
        self.assertTrue(newItem in player._inventory, errorMsg)
        self.assertTrue(newWeapon in player._inventory, errorMsg)
        self.assertTrue(newArmor in player._inventory, errorMsg)

        #Test removeFromInventory() default case
        player.removeFromInventory(newItem)
        player.removeFromInventory(newWeapon)
        player.removeFromInventory(newArmor)
        errorMsg = "Failed to remove item from inventory."
        self.assertFalse(newItem in player._inventory, errorMsg)
        self.assertFalse(newWeapon in player._inventory, errorMsg)
        self.assertFalse(newArmor in player._inventory, errorMsg)

        #Set things back up
        player._inventory = [newItem, newWeapon, newArmor]

        #Test that items are unequipped correctly
        player.removeFromInventory(newItem)
        player.removeFromInventory(newWeapon)
        player.removeFromInventory(newArmor)
        errorMsg = "Failed to remove item from equipped."
        self.assertFalse(newItem in player._equipped, errorMsg)
        self.assertFalse(newWeapon in player._equipped, errorMsg)
        self.assertFalse(newArmor in player._equipped, errorMsg)

        #Test that item-specific character attributes are reset to original values
        errorMsg = "_weaponAttack should be 0 but it is not."
        self.assertEqual(player._weaponAttack, 0, errorMsg)
        errorMsg = "_armorDefense should be 0 but it is not."
        self.assertEqual(player._armorDefense, 0, errorMsg)
        errorMsg = "_totalAttack should be player._attack but it is not."
        self.assertEqual(player._totalAttack, player._attack, errorMsg)

    def canMoveDirection(self):
        """
        Tests if canMoveDirection() methods work.
        """
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("Frodo", space)

        north = Space("North Space", "Very cold", "Welcome")
        south = Space("South Space", "Very warm", "Welcome")
        east = Space("East Space", "Very mountainous", "Welcome")
        west = Space("West Space", "Coastal", "Welcome")

        #Test negative case - no ports created
        errorMsg = "player.canMoveDirection() negative case failed."
        self.assertFalse(player.canMoveNorth(), errorMsg)
        self.assertFalse(player.canMoveSouth(), errorMsg)
        self.assertFalse(player.canMoveEast(), errorMsg)
        self.assertFalse(player.canMoveWest(), errorMsg)

        #Test positive case - ports created
        space.createExit("north", north, outgoingOnly = False)
        space.createExit("south", south, outgoingOnly = False)
        space.createExit("east", east, outgoingOnly = False)
        space.createExit("west", west, outgoingOnly = False)

        #Test negative case - no ports created
        errorMsg = "player.canMoveDirection() positive case failed."
        self.assertTrue(player.canMoveNorth(), errorMsg)
        self.assertTrue(player.canMoveSouth(), errorMsg)
        self.assertTrue(player.canMoveEast(), errorMsg)
        self.assertTrue(player.canMoveWest(), errorMsg)

class InnTest(unittest.TestCase):
    """
    Tests the healing ability of Inn Object.
    """
    def testCase(self):
        """
        For when player chooses to stay at Inn and has enough money to do so.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        #Player's health is lowest possible to be alive
        player._hp = 1
        #Player's money is equal to 10
        player._money = 10

        #Player chooses to stay at the inn
        rawInputMock = MagicMock(side_effect = ["yes", "leave city"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Player's money should decrease by the cost of the inn, in our case 5
        self.assertEqual(player._money, 5, "Player's money not decreased by correct amount.")
        
        #Player's health should increase to maximum
        self.assertEqual(player._hp, player._maxHp, "Player's health not increased to full health.")
        
    def testCase2(self):
        """
        For when player chooses to stay at Inn and does not have enough money to do so.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
                
        #Player's health is lowest possible to be alive
        player._hp = 1
        #Player's money is not enough to purchase services
        player._money = 2

        #Player chooses to stay at the inn
        rawInputMock = MagicMock(side_effect = ["yes", "leave city"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
        #Player's money remain at starting amount
        self.assertEqual(player._money, 2, "Player money changed when it should not have.")
        
        #Player's health should increase to maximum
        self.assertEqual(player._hp, 1, "Player's health changed when it should not have.")
        
    def testCase3(self):
        """
        For invalid user input.
        """
        from player import Player
        from space import Space
        from cities.inn import Inn
        from cities.city import City

        testInn = Inn("Chris' Testing Inn", "Come test here", "Hi", 5)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' Inn", testInn)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        #For invalid user input
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "gobbledigook", "gobbledigook", "no"])
        with patch('cities.inn.raw_input', create=True, new=rawInputMock):
            testInn.enter(player)
        
class ShopSellItems(unittest.TestCase):
    """
    Tests the ability to sell in the Shop Object:
    -Item should be removed from inventory and equipped objectSets
    -Player money should be increased by half of the value of the sold item
    -Item should be added to shop wares at full original cost

    TODO: test for invalid user input
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 5, 10)
        testShop._items = []
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        
        #Create starting iventory
        COST = 1
        weapon = Weapon("Knife", "Jack of all trades", 3, 1, COST)
        armor = Armor("Leather Tunic", "Travel cloak", 3, 1, COST)
        potion = Potion("Potion", "Vodka", 3, 1, COST)

        #Add items to player's inventory
        inventory = player._inventory
        player.addToInventory(weapon)
        player.addToInventory(armor)
        player.addToInventory(potion)
        self.assertTrue(inventory.containsItemWithName("Knife"), "Knife not added to inventory.")
        self.assertTrue(inventory.containsItemWithName("Leather Tunic"), "Leather Tunic not added to inventory.")
        self.assertTrue(inventory.containsItemWithName("Potion"), "Potion not added to inventory.")

        #Equip items and test to see that items are equipped
        equipped = player.getEquipped()
        player.equip(weapon)
        player.equip(armor)
        errorMsg = "Player items were not equipped correctly."
        self.assertTrue(equipped.containsItem(weapon), errorMsg)
        self.assertTrue(equipped.containsItem(armor), errorMsg)
                        
        #Player chooses to: sell items, to sell knife, yes, quit the shop
        rawInputMock = MagicMock(side_effect = ["sell", "Knife", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Player chooses to: sell items, to sell leather tunic, yes, quit the shop
        rawInputMock = MagicMock(side_effect = ["sell", "Leather Tunic", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Player chooses to: sell items, to sell potion, yes, quit the shop
        rawInputMock = MagicMock(side_effect = ["sell", "Potion", "yes", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
        
        #Player's inventory should no longer include items
        self.assertFalse(inventory.containsItemWithName("Knife"), "Knife that was sold is still in inventory")
        self.assertFalse(inventory.containsItemWithName("Leather Tunic"), "Leather tunic that was sold is still in inventory")
        self.assertFalse(inventory.containsItemWithName("Potion"), "Potion that was sold is still in inventory")

        #Player equipped should no longer include items
        self.assertFalse(equipped.containsItemWithName("Knife"), "Knife that was sold is still in equipped")
        self.assertFalse(equipped.containsItemWithName("Leather Tunic"), "Leather tunic that was sold is still in equipped")

        #Items now appear in shop wares
        errorMsg = "Items are now supposed to be in shop inventory but are not."
        self.assertTrue(weapon in testShop._items, errorMsg)
        self.assertTrue(armor in testShop._items, errorMsg)
        self.assertTrue(potion in testShop._items, errorMsg)

        #Player's money should increase by the half the cost of the items. In our case, it should increase by 1.5
        self.assertEqual(player._money, 21.5, "Player's money not increased by correct amount. It is %s." % player._money)

        #Item prices are normal prices, not sell value
        errorMsg = "Item costs were not set back to where they were supposed to be."
        for item in testShop._items:
            self.assertEqual(item._cost, COST, errorMsg)
        
        #Player chooses to: gobbledigook, quit the shop - context menus should not crash program
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

class ShopPurchaseItems(unittest.TestCase):
    """
    Tests the ability to purchase items in the Shop:
    1) Purchasing an item player has money for
        -Item in inventory, not in equipped, not in shop wares, money changed by correct amount
    2) Failing to purchase an item player does not have money for
        -Item not in inventory, not in equipped, in shop wares, money unchanged
    3) Failing to purchase invalid item
        -Item not in inventory, not in equipped, money unchanged
    4) Invalid user input does not crash game

    TODO: test for invalid user input
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.shop import Shop
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion

        testShop = Shop("Chris' Testing Shop", "Come test here", "Hi", 5, 10)
        testCity = City("Test City", "Testing city", "Hello to testing city. See Chris' shop", testShop)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
       
        #Our shop should currently have five items (this was designed when it was created)
        self.assertEqual(len(testShop._items), 5, "Our test shop was generated with the wrong number of items")
        errorMsg = "Items in shop inventory are of wrong type."
        for item in testShop._items:
            self.assertTrue(isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Potion), errorMsg)

        #Add Weapon to Shop inventory  with weight=1, healing=1, cost=1
        testWeapon = Potion("Knife", "Russian", 1, 1, 1)
        testShop._items.append(testWeapon)
        
        #Add Armor to Shop inventory  with weight=1, healing=1, cost=1
        testArmor = Potion("Shield of Faith", "Also Russian", 1, 1, 1)
        testShop._items.append(testArmor)
        
        #Add Potion to Shop inventory with weight=1, healing=5, cost=3
        testPotion = Potion("Medium Potion of Healing", "A good concoction. Made by Master Wang.", 1, 5, 3)
        testShop._items.append(testPotion)
       
        #Player should start with 20 rubles
        player._money = 20
        self.assertEqual(player._money, 20, "Player does not start with 20 rubles")

        #Player chooses to: purchase item, "Knife" (purchase this specific item), quit the shop
        rawInputMock = MagicMock(side_effect = ["purchase", "Knife", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)

        #Player chooses to: purchase item, "Shield of Faith" (purchase this specific item), quit the shop
        rawInputMock = MagicMock(side_effect = ["purchase", "Shield of Faith", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player chooses to: purchase item, "Medium Potion of Healing" (purchase this specific item), quit the shop
        rawInputMock = MagicMock(side_effect = ["purchase", "Medium Potion of Healing", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should decrease by the cost of the purchases, which is 5 (1+1+3)
        self.assertEqual(player._money, 15, "Player's money not decreased by correct amount. It is %s." % player._money)

        #Test item in inventory, not in equipped, not in shop wares - testWeapon
        errorMsg = "Knife that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Knife that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Knife"), errorMsg)
        errorMsg = "Knife that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)

        #Test item in inventory, not in equipped, not in shop wares - testArmor
        errorMsg = "Shield of Faith that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Shield of Faith"), errorMsg)
        errorMsg = "Shield of Faith that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Shield of Faith"), errorMsg)
        errorMsg = "Shield of Faith that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)
        
        #Test item in inventory, not in equipped, not in shop wares - testPotion
        errorMsg = "Medium Potion that was purchased was not added to inventory."
        self.assertTrue(player._inventory.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Medium Potion of Healing"), errorMsg)
        errorMsg = "Medium Potion that was purchased is still in shop wares."
        self.assertFalse(testPotion in testShop._items, errorMsg)
        
        #Add SuperDuperLegendary Potion to Shop inventory with weight=1, healing=35, cost=28
        testPotion2 = Potion("SuperDuperLegendary Potion of Healing", "A Wang concoction. Made by Master Wang.", 1, 35, 28)
        testShop._items.append(testPotion2)

        #Player chooses to: purchase item, "SuperDuperLegendary Potion of Healing", quit the shop
        rawInputMock = MagicMock(side_effect = ["purchase", "SuperDuperLegendary Potion of Healing", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should not decrease by the cost of SuperDuperLegendary Potion of Healing, which is 28
        errorMsg = "Player's money should not be decreased from 15. Player can't buy SuperDuperLegendary Potion. It is currently %s." % player._money
        self.assertEqual(player._money, 15, errorMsg)
       
        #Test item not in inventory, not in equipped, in shop wares
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased was added to inventory."
        self.assertFalse(player._inventory.containsItemWithName("SuperDuperLegendary Potion of Healing"), errorMsg)
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("SuperDuperLegendary Potion of Healing"), errorMsg)
        errorMsg = "SuperDuperLegendary Potion of Healing that was purchased is no longer in shop wares."
        self.assertTrue(testPotion2 in testShop._items, errorMsg)

        #Player chooses to: purchase item, input "Fake Item", quit the shop
        rawInputMock = MagicMock(side_effect = ["purchase", "Fake Item", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
       
        #Player's money should not change
        errorMsg = "Player's money should not be decreased when trying to purchase fake item. It is currently %s" % player._money
        self.assertEqual(player._money, 15, errorMsg)
       
        #Test item not in inventory, not in equipped
        errorMsg = "Fake Item that was purchased was added to inventory."
        self.assertFalse(player._inventory.containsItemWithName("Fake Item"), errorMsg)
        errorMsg = "Fake Item that was purchased is in equipped."
        self.assertFalse(player._equipped.containsItemWithName("Fake Item"), errorMsg)
            
        #Player chooses to: gobbledigook, quit the shop
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "quit"])
        with patch('cities.shop.raw_input', create = True, new = rawInputMock):
            testShop.enter(player)
            
        #TODO make test for verifying the stats of items in the shop, and put into 1 shop test class with multiple methods
            
class Square(unittest.TestCase):
    """
    Tests Square objects. Test that gift items get added to inventory and removed from square._items.

    Three cases:
    -Person has several items to give (Master Wang).
    -Person has one item to give (Miles).
    -Person has no items to give (Putin).
    -Invalid user input (gobbledigook).
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from cities.square import Square
        from cities.city import City
        from items.weapon import Weapon
        from items.armor import Armor
        from items.potion import Potion
        from items.item import Item

        weapon = Weapon("Sword of the Spirit", "Sharper than any double-edged sword", 1, 1, 1)
        armor = Armor("Shield of Faith", "Quenches fiery darts", 1, 1, 1)
        potion = Potion("Leaves from Tree of Life", "For healing the nations", 1, 1, 1)
        cookies = Item("Miles' Famous Cookies", "Gross this time", 1)
        
        talk = {"Master Wang": "I am Master Wang, creator various things in this Lord of the Rings game", "Miles": "Hello, I am Miles, the cookie legend", "Putin": "Oppression, engage...."}
        items = {"Master Wang": [weapon, armor, potion], "Miles": cookies}
        testSquare = Square("Chris' Testing Square", "Testing Square", "Come test here", talk, items)
        
        testCity = City("Test City", "Testing city", "Hello to Test City. See Chris' Square", testSquare)
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)
        inventory = player.getInventory()
        
        #Player chooses to talk to Master Wang, quit
        rawInputMock = MagicMock(side_effect = ["Master Wang", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)

        #Check that items associated with Master Wang are now in inventory
        errorMsg = "Weapon is supposed to be in inventory but is not."
        self.assertTrue(weapon in inventory, errorMsg)
        errorMsg = "Armor is supposed to be in inventory but is not."
        self.assertTrue(armor in inventory, errorMsg)
        errorMsg = "Potion is supposed to be in inventory but is not."
        self.assertTrue(potion in inventory, errorMsg)

        #Check that items are no longer in square._items
        errorMsg = "Weapon is not supposed to be in testSquare._items but is."
        self.assertFalse(weapon in testSquare._items, errorMsg)
        errorMsg = "Armor is not supposed to be in testSquare._items but is."
        self.assertFalse(armor in testSquare._items, errorMsg)
        errorMsg = "Potion is not supposed to be in testSquare._items but is."
        self.assertFalse(potion in testSquare._items, errorMsg)

        #Player chooses to talk to Miles, quit
        rawInputMock = MagicMock(side_effect = ["Miles", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)

        #Check that item associated with Miles is now in inventory
        errorMsg = "Cookies is supposed to be in inventory but is not."
        self.assertTrue(cookies in inventory, errorMsg)

        #Check that item is no longer in square._items
        errorMsg = "Cookies is not supposed to be in testSquare._items but is."
        self.assertFalse(cookies in testSquare._items, errorMsg)

        #Player chooses to talk to Putin, quit
        rawInputMock = MagicMock(side_effect = ["Putin", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)

        #For invalid user input, quit
        rawInputMock = MagicMock(side_effect = ["gobbledigook", "quit"])
        with patch('cities.square.raw_input', create = True, new = rawInputMock):
            testSquare.enter(player)
   
class City(unittest.TestCase):
    """
    Tests the ability of City object to handle a series of commands.
    """
    def testInit(self):
        from player import Player
        from space import Space
        from cities.city import City
        from cities.inn import Inn
        from cities.shop import Shop
        from cities.square import Square
        
        testInn = Inn("Seth N' Breakfast Test Inn", "Testing inn", "Come test here", 3)
        testShop = Shop("Russian Armory", "Many guns", "?", 5, 5)
        testSquare = Square("Kremlin", "In Moscow", "?")
        testCity = City("TestCity","Chris' unique testing city", "Come test here", buildings = [testInn, testShop, testSquare])
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity)
        player = Player("Frodo", space)

        #Player chooses to: enter testInn, leave, enter testShop, leave, enter testSquare, leave, "gobbledigook", leave city
        cityInputMock = MagicMock(side_effect = ["Seth N' Breakfast Test Inn", "leave city", "Russian Armory",
            "leave city", "Kremlin", "gobbledigook", "leave city"])
        innInputMock = MagicMock(side_effect = ["no"])
        shopInputMock = MagicMock(side_effect = ["quit"])
        squareInputMock = MagicMock(side_effect = ["quit"])
        
        with patch('cities.city.raw_input', create = True, new = cityInputMock):
            with patch('cities.inn.raw_input', create = True, new = innInputMock):
                testCity.enter(player)
            with patch('cities.shop.raw_input', create = True, new = shopInputMock):
                testCity.enter(player)
            with patch('cities.square.raw_input', create = True, new = squareInputMock):
                testCity.enter(player)
        
class UniquePlace(unittest.TestCase):
    """
    Tests for correct unique place initialization.
    """
    def testEnter(self):
        from player import Player
        from space import Space
        from unique_place import UniquePlace

        testUniquePlace = UniquePlace("Chris' Unique Testing Room", "Come test here", "Here's some chocolate for coming")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", uniquePlace = testUniquePlace)
        player = Player("Frodo", space)

        errorMsg = "._name was not initialized correctly."
        self.assertEqual(testUniquePlace._name, "Chris' Unique Testing Room", errorMsg)
        errorMsg = "._description was not initialized correctly."
        self.assertEqual(testUniquePlace._description, "Come test here", errorMsg)
        errorMsg = "._greetings was not initialized correctly."
        self.assertEqual(testUniquePlace._greetings, "Here's some chocolate for coming", errorMsg)

class EnterCommand(unittest.TestCase):
    """
    Tests for Enter Command. In these tests, player executes enterCmd on a variety
    of different combinations of places.

    Iterations:
    testCase1: no cities or unique places to enter.
    testCase2: one city and one unique place to enter.
    testCase3: multiple cities and one unique place to enter.
    testCase4: one city and multiple cities to enter.
    testCase5: multiple cities and multiple unique places to enter.
    testCase6: invalid user input.
    """
    def testCase1(self):
        """
        Trying to enter when there is nothing to enter (no cities or unique places).
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to enter when there are no places to enter
        rawInputMock = MagicMock(side_effect = ["enter"])
        with patch('commands.enter_command.raw_input', create = True, new = rawInputMock):
            enterCmd.execute()
                
    def testCase2(self):
        """
        One city and one unique places.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testUniquePlace = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = testCity, uniquePlace = testUniquePlace)
        player = Player("The Funlaps", space)
        
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to go to testCity, leave, testUniquePlace, stop
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Master Wang's Magical Testing Place"])
        cityInputMock = MagicMock(side_effect = ["leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testCase3(self):
        """
        Multiple cities, one unique place.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testCity2 = City("Seth's Sans-Shabbiness Shack Sh-City", "Seth's unique testing city", "Come test here")
        testCity3 = City("Miles' Magical Cookie Jail City", "Miles' unique testing city", "Come test here")
        testUniquePlace = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = [testCity1, testCity2, testCity3], uniquePlace = testUniquePlace)
        player = Player("The Funlaps", space)
        
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to go to testCity1, leave, testCity2, leave, testCity3, leave, testUniquePlace, stop
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Seth's Sans-Shabbiness Shack Sh-City", 
            "Miles' Magical Cookie Jail City", "Master Wang's Magical Testing Place", "stop"])
        cityInputMock = MagicMock(side_effect = ["leave city", "leave city", "leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testCase4(self):
        """
        One city, multiple unique places.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testUniquePlace1 = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        testUniquePlace2 = UniquePlace("Jim's Magic Castle of Time-Shifting", "Many different colours", "What time is it?")
        testUniquePlace3 = UniquePlace("Russian Armadillo Mound", "Where Texas meets Russia", "I'm confused.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = testCity, uniquePlace = [testUniquePlace1, testUniquePlace2, testUniquePlace3])
        player = Player("The Funlaps", space)
        
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to go to testCity, leave, testUniquePlace1, leave, testUniquePlace2, leave, testUniquePlace3, stop
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Master Wang's Magical Testing Place", 
            "Jim's Magic Castle of Time-Shifting", "Russian Armadillo Mound", "stop"])
        cityInputMock = MagicMock(side_effect = ["leave city", "leave city", "leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()

    def testCase5(self):
        """
        Multiple cities and unique places.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Jim's Mobile Fun City", "Jim's unique testing city", "Come test here")
        testCity2 = City("Seth's Sans-Shabbiness Shack Sh-City", "Seth's unique testing city", "Come test here")
        testCity3 = City("Miles' Magical Cookie Jail City", "Miles' unique testing city", "Come test here")
        testUniquePlace1 = UniquePlace("Master Wang's Magical Testing Place", "Come test here", "Hi I'm made of cheese.")
        testUniquePlace2 = UniquePlace("Jim's Magic Castle of Time-Shifting", "Many different colours", "What time is it?")
        testUniquePlace3 = UniquePlace("Russian Armadillo Mound", "Where Texas meets Russia", "I'm confused.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor",
            city = [testCity1, testCity2, testCity3], uniquePlace = [testUniquePlace1, testUniquePlace2, testUniquePlace3])
        player = Player("The Funlaps", space)
        
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to go to testCity1, leave, testCity2, leave, testCity3, leave, testUniquePlace1,
        #leave, testUniquePlace2, leave, testUniquePlace3, stop
        spaceInputMock = MagicMock(side_effect = 
            ["Jim's Mobile Fun City", "Seth's Sans-Shabbiness Shack Sh-City", 
            "Miles' Magical Cookie Jail City", "Master Wang's Magical Testing Place",
            "Jim's Magic Castle of Time-Shifting", "Russian Armadillo Mound", "stop"])
        cityInputMock = MagicMock(side_effect = ["leave city", "leave city", "leave city", "leave city", "leave city"])
        with patch('commands.enter_command.raw_input', create = True, new = spaceInputMock):
            with patch('cities.city.raw_input', create = True, new = cityInputMock):
                enterCmd.execute()
                
    def testCase6(self):
        """
        Invalid user input.
        """
        from space import Space
        from commands.enter_command import EnterCommand
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("The Funlaps", space)
        enterCmd = EnterCommand("Enter Command", "Tests Entering", player)
        
        #Player chooses to enter "Jdlskfjsd City", stop entering a city
        rawInputMock = MagicMock(side_effect = ["enter", "Jdlskfjsd City", "stop"])
        with patch('commands.enter_command.raw_input', create = True, new = rawInputMock):
            enterCmd.execute()

class DescribeCommand(unittest.TestCase):
    """
    Tests Describe Command.
    
    Three cases:
    -Works with space and no cities/unique places.
    -Works with one city and one unique place.
    -Works with multiple cities and multiple unique places.
    """
    def testCase1(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        
        space = Space("Shire", "Home of the Hobbits.", "Mordor")
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()
    
    def testCase2(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity = City("Master Wang's Oriental Fun City", "Chris's testing city", "Come test here")
        testUniquePlace = UniquePlace("The UniquePlace of Testing", "Weird things sometimes happen when you test.", "Welcome to UniquePlace of Testing.")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = testCity, uniquePlace = testUniquePlace)
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()

    def testCase3(self):
        from space import Space
        from commands.describe_command import DescribeCommand
        from player import Player
        from space import Space
        from cities.city import City
        from unique_place import UniquePlace
        
        testCity1 = City("Master Wang's Oriental Fun City", "Chris' unique testing city", "Come test here")
        testCity2 = City("Chocolate Mountain", "Next to Vanilla Mountain", "Hi I'm Jim")
        testUniquePlace1 = UniquePlace("The UniquePlace of Testing", "Weird things sometimes happen when you test.", "Welcome to UniquePlace of Testing.")
        testUniquePlace2 = UniquePlace("Ukraine", "Not in great shape", "Welcome to Ukraine")
        space = Space("Shire", "Home of the Hobbits.", "Mordor", city = [testCity1, testCity2], uniquePlace = [testUniquePlace1, testUniquePlace2])
        player = Player("The Bagginses", space)
        describeCmd = DescribeCommand("Test Describe Command", "Tests Describing", player)
        
        describeCmd.execute()

class monster(unittest.TestCase):
    """
    Tests Monster class.
    """
    def testMonster(self):
        from monsters.monster import Monster

        monster = Monster("Jack", "@$$", [10, 5, 7], "Moof", "Meep")

        #Test monster initialized correctly
        errorMsg = "monster._name should be 'Jack'"
        self.assertEqual(monster._name, "Jack", errorMsg)
        errorMsg = "monster._description should be '@$$'"
        self.assertEqual(monster._description, "@$$", errorMsg)
        errorMsg = "monster._hp should be 10"
        self.assertEqual(monster._hp, 10, errorMsg)
        errorMsg = "monster._attack should be 5"
        self.assertEqual(monster._attack, 5, errorMsg)
        errorMsg = "monster._experience should be 7"
        self.assertEqual(monster._experience, 7, errorMsg)
        errorMsg = "monster._attackString sound be 'Moof'"
        self.assertEqual(monster._attackString, "Moof", errorMsg)
        errorMsg = "monster._deathString should be 'Meep'"
        self.assertEqual(monster._deathString, "Meep", errorMsg)
        
        #Test monster.attack()
        player = MagicMock()
        player.takeAttack = MagicMock()
        
        monster.attack(player)
        errorMsg = "monster.attack() failed to carry attack to player."
        player.takeAttack.assert_called_with(5)

        #Test monster.takeAttack() - attack is less than total hp
        monster.takeAttack(3)
        errorMsg = "monster.takeAttack() testcase #1 failed."
        self.assertEqual(monster._hp, 7, errorMsg)

        #Test monster.takeAttack() - attack is more than total hp
        monster.takeAttack(1000)
        errorMsg = "monster.takeAttack() testcase #2 failed"
        self.assertEqual(monster._hp, 0, errorMsg)

class monsterFactory(unittest.TestCase):
    """
    Tests monster factory.

    Pieces:
    -Tests default monster creation, that monsters are in fact created.
    -Testing difficulty feature - that default stats are implemented when
    difficulty set to zero. 
    -Testing difficulty feature - that monster stats increase as
    percentage over default. For instance, difficulty = 1 should result
    in monsters with 200% base monster stats.
    -Testing difficulty feature - that default monster spawn occurs when
    difficulty is set to zero.
    -Testing difficulty feature - that monster spawn increases as a percentage
    over default. For instance, difficulty = 1 should result in a 100% increase
    in monster spawn over base.
    -Testing that regional spawns work: that monster spawn reflects
    regional monster distributions held in constants. 

    Note params for getMonster: getMonsters(number, region, difficulty).
    """
    def defaultMonsterCreation(self):
        #Tests default monster creation, that monsters are in fact created.
        from factories.monster_factory import getMonsters
        from monsters.monster import Monster
        
        monsters = getMonsters(3, 1, 0)
        errorMsg = "Nothing was created in initial monster creation test."
        self.assertTrue(len(monsters) != 0, errorMsg)
        
        for monster in monsters:
            errorMsg = "getMonsters did not spawn Monster objects."
            self.assertTrue(isinstance(monster, Monster), errorMsg)

    def defaultStatGeneration(self):
        #Testing difficulty feature - that default stats are implemented when
        #difficulty set to zero.
        """
        Mocked up monster spawn distribution of ERIADOR such that Trolls are spawned
        100% of the time. getMonsters is to spawn three Trolls using the newly mocked
        up monster distribution.
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        import constants
        
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: 1})
        monsters = getMonsters(3, 1, 0)
        for monster in monsters:
            errorMsg = "monster._hp was not initiated correctly."
            self.assertEqual(monster._hp, constants.MONSTER_STATS[Troll][0], errorMsg)
            errorMsg = "monster._attack was not initiated correctly."
            self.assertEqual(monster._attack, constants.MONSTER_STATS[Troll][1], errorMsg)
            errorMsg = "monster._experience was not initiated correctly."
            self.assertEqual(monster._attack, constants.MONSTER_STATS[Troll][2], errorMsg)
            
    def difficultyBonusStats(self):
        #-Testing difficulty feature - that monster stats increase as
        #percentage over default. For instance, difficulty = 1 should result
        #in monsters with 200% base monster stats.
        """
        Mocked up monster distribution of ERIADOR such that Trolls are spawned 100%
        of the time. getMonsters is to spawn Trolls with 200% base stats. 
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        import constants
        
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: 1})
        monsters = getMonsters(3, 1, 1)
        for monster in monsters:
            errorMsg = "monster._hp was not initiated correctly."
            self.assertEqual(monster._hp, 2 * constants.MONSTER_STATS[Troll][0], errorMsg)
            errorMsg = "monster._attack was not initiated correctly."
            self.assertEqual(monster._attack, 2 * constants.MONSTER_STATS[Troll][1], errorMsg)
            errorMsg = "monster._experience was not initiated correctly."
            self.assertEqual(monster._attack, 2 * constants.MONSTER_STATS[Troll][2], errorMsg)
            
    def defaultSpawnNumber(self):    
        #-Testing difficulty feature - that default monster spawn occurs when
        #difficulty is set to zero.
        """
        Params: number = 3, region = 1 (ERIADOR), difficulty = 0.
        """
        from factories.monster_factory import getMonsters
        
        monsters = getMonsters(3, 1, 0)
        
        errorMsg = "getMonsters did not spawn three monsters."
        self.assertEqual(len(monsters), 3, errorMsg)

    def difficultyBonusSpawn(self):
        #-Testing difficulty feature - that monster spawn increases as a percentage
        #over default. For instance, difficulty = 1 should result in a 100% increase
        #in monster spawn over base. 
        """
        Params: number = 3, region = 1 (ERIADOR), difficulty = 1.

        Six monsters should be spawned: (3 + (3 * 100%)).
        """
        from factories.monster_factory import getMonsters
        
        monsters = getMonsters(3, 1, 1)
        
        errorMsg = "getMonsters did not spawn six monsters."
        self.assertEqual(len(monsters), 6, errorMsg)

    def regionalSpawn(self):
        #-Testing that regional spawns work: that monster spawn reflects
        #regional monster distributions held in constants. 
        """
        Tests that monsters of each type in a region's distribution
        spawn, given a large enough sample size.
        """
        from factories.monster_factory import getMonsters
        from monsters.troll import Troll
        from monsters.nazgul import Nazgul
        from monsters.goblin import Goblin
        from monsters.great_goblin import GreatGoblin
        import constants
            
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Troll: .25,
            Nazgul: 1})
        constants.RegionMonsterDistribution = MagicMock(ERIADOR = {Goblin: .8,
            GreatGoblin: 1})

        monstersEriador = getMonsters(5000, 1, 0)
        monstersHighPass = getMonsters(5000, 3, 0)

        #Checking to see that Nazgul and Trolls are spawned
        numberNazgul = 0
        numberTroll = 0
        for monster in monstersEriador:
            if isinstance(monster, Nazgul):
                numberNazgul += 1
            elif isinstance(monster, Troll):
                numberTroll += 1
            else:
                raise AssertionError("Invalid monster type")

        errorMsg = "No nazgul spawned."
        self.assertTrue(numberNazgul != 0, errorMsg)
        errorMsg = "No trolls spawned."
        self.assertTrue(numberTroll != 0, errorMsg)

        #Checking to see that Goblin and GreatGoblin are spawned
        numberGoblin = 0
        numberGreatGoblin = 0
        for monster in monstersHighPass:
            if isinstance(monster, Goblin):
                numberGoblin += 1
            elif isinstance(monster, GreatGoblin):
                numberGreatGoblin += 1
            else:
                raise AssertionError("Invalid monster type")

        errorMsg = "No goblins spawned."
        self.assertTrue(numberGoblin != 0, errorMsg)
        errorMsg = "No great goblins spawned."
        self.assertTrue(numberGreatGoblin != 0, errorMsg)
    
class battleEngine(unittest.TestCase):
    """
    Tests battleEngine.    
    """
    pass

def handle_pdb(signal, frame):
    """
    Signal handler method that invokes pdb.

    @param signal:      Signal
    @param frame:       Frame
    """
    import pdb
    pdb.Pdb().set_trace(frame)

if __name__ == '__main__':
    #Add signal handler that invokes PDG
    signal.signal(signal.SIGINT, handle_pdb)

    #Supress output from game with "buffer=true"
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
